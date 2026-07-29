from django.test import TestCase


class TemplateRenderingTests(TestCase):
    def test_akhil_page_renders_sample_template(self):
        response = self.client.get('/akhil/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This is my first Repository')
