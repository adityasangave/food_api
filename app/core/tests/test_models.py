from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email="test@123", password="12356"):
    return get_user_model().objects.create_user(email, password)

class model_test(TestCase):

    def test_create_user_with_email_pass(self):
        """Test that user is getting created successfully using email and password"""
        email = "test@gmail.com"
        password = "test123"

        user=get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@LONDONAPPDEV.com'
        user = get_user_model().objects.create_user(email, 'test123')
        
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@londonappdev.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        tag = models.Tag.objects.create(
            user = sample_user(),
            name = "vegan"
        )

        self.assertTrue(str(tag), tag.name)

    def test_ingredient_model(self):
        ingredient = models.Ingredient .objects.create(
            user = sample_user(),
            name = "Hot dog"
        )

        self.assertEqual(str(ingredient), ingredient.name)