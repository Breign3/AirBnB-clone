!#/usr/bin/python3

# tests/test_base_model.py

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """Set up for the tests"""
        self.model = BaseModel()

    def test_id(self):
        """Test if id is a string"""
        self.assertIsInstance(self.model.id, str)

    def test_uuid(self):
        """Test if id is a valid uuid"""
        try:
            uuid.UUID(self.model.id, version=4)
        except ValueError:
            self.fail("id is not a valid uuid")

    def test_created_at(self):
        """Test if created_at is a datetime object"""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at(self):
        """Test if updated_at is a datetime object"""
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save(self):
        """Test if save method updates updated_at"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()

