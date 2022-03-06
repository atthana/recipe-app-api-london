from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.Client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@engineer.com',
            password='password123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@engineer.com',
            password='password123',
            name='Test user full name'
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')  # url แบบนี้ก้อมาจากใน doc นั่นแหละ หรือเราจะ show_urls ดูก้อได้นะ
        res = self.client.get(url)

        self.assertContains(res, self.user.name)  # เช็คว่า response มันมี name กับ email อยุ่ด้วยรึป่าว
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])  # /admin/core/user/1
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
