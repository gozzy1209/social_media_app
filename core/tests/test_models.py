# tests/test_models.py
import pytest
from django.contrib.auth import get_user_model
from .models import LikePost, Post, Profile,FollowersCount
from datetime import datetime

User = get_user_model()

@pytest.mark.django_db
def test_profile_model():
    user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
    profile = Profile.objects.create(user=user, id_user=user.id, bio='Test bio', location='Test location')
    assert profile.user == user
    assert profile.bio == 'Test bio'
    assert profile.location == 'Test location'

@pytest.mark.django_db
def test_post_model():
    user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
    post = Post.objects.create(user='testuser', caption='Test caption')
    assert post.user == 'testuser'
    assert post.caption == 'Test caption'

@pytest.mark.django_db
def test_likepost_model():
    post = Post.objects.create(user='testuser', caption='Test caption')
    like = LikePost.objects.create(post_id=post.id, username='testuser')
    assert like.post_id == post.id
    assert like.username == 'testuser'

@pytest.mark.django_db
def test_followerscount_model():
    follower = 'testfollower'
    user = 'testuser'
    count = FollowersCount.objects.create(follower=follower, user=user)
    assert count.follower == follower
    assert count.user == user
