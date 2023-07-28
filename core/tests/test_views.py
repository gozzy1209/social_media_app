# tests/test_views.py
import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client
from .models import LikePost, Post, Profile,FollowersCount

@pytest.fixture
def client():
    return Client()

@pytest.mark.django_db
def test_index_view(client):
    user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
    profile = Profile.objects.create(user=user, id_user=user.id, bio='Test bio', location='Test location')
    client.force_login(user)
    response = client.get(reverse('index'))
    assert response.status_code == 200
    assert 'user_profile' in response.context
    assert 'posts' in response.context
    assert 'suggestions_username_profile_list' in response.context
    assert response.context['user_profile'] == profile

# Add more view tests for other views as needed.
