from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient


class GetBooksViewTest(TestCase):

    def setUp(self) -> None:
        self.endpoint = '/library/books/'
        self.client = APIClient()
        
    def _get(self, data={}):
        return self.client.get(self.endpoint, data=data)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/library/books/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('books_view'))
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        response = self.client.get(reverse('books_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_list.html')
