from django.test import TestCase
from Restaurant.models import Menu
#TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Stromboli", price=16.99, inventory=50)
        self.assertEqual(item, "Stromboli : 16.99")