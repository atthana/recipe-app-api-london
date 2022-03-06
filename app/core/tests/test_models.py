from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'grassroot@engineer.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)  # เช็คว่า email มันถูกต้อง
        self.assertTrue(user.check_password(password))  # เช็ค password ว่าถูกต้องไหม