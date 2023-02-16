from django.test import TestCase
from .models import Project


class ProjectModelTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title="Test project",
            description="This is a test project",
            url="https://www.example.com"
        )

    def test_project_title(self):
        self.assertEqual(self.project.title, "Test project")

    def test_project_description(self):
        self.assertEqual(self.project.description, "This is a test project")

    def test_project_url(self):
        self.assertEqual(self.project.url, "https://www.example.com")

    def test_project_image(self):
        self.assertIsNotNone(self.project.image)
