import unittest
import tempfile
import os
from clean_data_module_Copy1 import clean_data_from_file  # Replace 'your_module' with the actual module name.

class TestCleanDataFromFile(unittest.TestCase):
    def create_temp_file(self, content):
        """
        Helper function to create a temporary file with the given content.
        Returns the file path.
        """
        tmp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8')
        tmp_file.write(content)
        tmp_file.close()
        return tmp_file.name

    def test_valid_numbers(self):
        """
        Test that valid numbers are correctly extracted.
        """
        # The content includes valid numbers and some tokens that should be ignored.
        content = "3.14 42 -2.718 some_text 3.14abc +.75 .5 -7"
        # Expected valid numbers: 3.14, 42, -2.718, +.75, .5, and -7
        expected = [3.14, 42.0, -2.718, 0.75, 0.5, -7.0]

        file_path = self.create_temp_file(content)
        try:
            result = clean_data_from_file(file_path)
            self.assertEqual(result, expected)
        finally:
            print(result)
            input(file_path)
            os.remove(file_path)

    def test_empty_file(self):
        """
        Test that an empty file returns an empty list.
        """
        content = ""
        expected = []

        file_path = self.create_temp_file(content)
        try:
            result = clean_data_from_file(file_path)
            self.assertEqual(result, expected)
        finally:
            input(file_path)
            os.remove(file_path)

    def test_numbers_with_extra_characters(self):
        """
        Test that tokens which are not exactly valid numbers are ignored,
        even if they contain valid number characters.
        """
        # All tokens here include extra characters that invalidate them as numbers.
        content = "123abc abc123 456.789! 0.001, -5.6? +7#"
        expected = []  # None of these tokens should be interpreted as valid numbers.

        file_path = self.create_temp_file(content)
        try:
            result = clean_data_from_file(file_path)
            self.assertEqual(result, expected)
        finally:
            input(file_path)
            os.remove(file_path)

    def test_numbers_with_whitespace_variations(self):
        """
        Test that the function correctly parses numbers regardless of
        the whitespace (tabs, newlines, etc.) separating tokens.
        """
        content = "3.14\t42\n-2.718  \t +.75\n.5    -7"
        expected = [3.14, 42.0, -2.718, 0.75, 0.5, -7.0]

        file_path = self.create_temp_file(content)
        try:
            result = clean_data_from_file(file_path)
            self.assertEqual(result, expected)
        finally:
            input(file_path)
            os.remove(file_path)

if __name__ == '__main__':
    unittest.main()
