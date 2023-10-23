from django.test import TestCase


class SimpleTestCase(TestCase):
    def test_s1(self):
        self.assertEqual(5*5, 25)

    def test_s2(self):
        self.assertEqual(5/5, 1)
