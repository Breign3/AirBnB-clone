#!/usr/bin/python3

import unittest
from datetime import datetime
from base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_id_generation(self):
        # Check if id is generated and is a string
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at(self):
        # Check if created_at is a datetime object
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at(self):
        # Check if updated_at is a datetime object
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str_representation(self):
        # Check if __str__ method returns the expected string
        expected_output = "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_output)

    def test_save_method(self):
        # Check if save method updates updated_at
        previous_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(previous_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        # Check if to_dict method returns the expected dictionary
        expected_dict = {
            'id': self.base_model.id,
            'created_at': self.base_model.created_at.isoformat(),
            'updated_at': self.base_model.updated_at.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertEqual(self.base_model.to_dict(), expected_dict)

if __name__ == '__main__':
    unittest.main()

