from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post


class BlogTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123')
        testuser1.save()

    # Create a blog post

        test_post = Post.objects.create(

        )