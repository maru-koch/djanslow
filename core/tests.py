from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from core.models import Customer
from django.urls import reverse
# Create your tests here.

class SimpleTest(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        
    def test_assert_into_db(self):
        client = APIClient()
        path = reverse('add')
        payload = {'name':'Kio rant', 'sex':'Female', 'address':'Ademuno'}
        response = client.post(path, payload)
        self.assertTrue(response.status_code, 201)
        