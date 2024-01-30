from django.db import models
"""
At the top we’re importing the class models and then creating a subclass of models.Model
called Post. Using this subclass functionality we automatically have access to everything
within django.db.models.Models and can add additional fields and methods as
desired.

For title we’re limiting the length to 200 characters  
For body we’re using a TextField which will automatically expand as needed to fit the user’s text. 

For the author field we’re using a ForeignKey which allows for a many-to-one relationship.
This means that a given user can be the author of many different blog posts
but not the other way around. The reference is to the built-in User model that Django
provides for authentication. For all many-to-one relationships such as a ForeignKey
we must also specify an on_delete option.
"""

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title
