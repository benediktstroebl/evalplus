Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

This removes all vowels (both uppercase and lowercase) from the text using the `translate` method and `str.maketrans` to create a translation table that removes all instances of vowels.

It is defined within a module (`remove_vowels.py`) so that it can be distributed as a standalone file, and it includes a simple test suite to verify its behavior:
```python
import unittest
from remove_vowels import remove_vowels

class TestRemoveVowels(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_vowels(""), "")

    def test_string_without_vowels(self):
        self.assertEqual(remove_vowels("bcdf\nghjklm"), "bcdf\nghjklm")

    def test_string_with_vowels(self):
        self.assertEqual(remove_vowels("abcdef"), "bcdf")

    def test_string_with_multiple_vowels(self):
        self.assertEqual(remove_vowels("aaaaa"), "")

    def test_string_with_mixed_characters(self):
        self.assertEqual(remove_vowels("aaBAA"), "B")

    def test_string_with_non_ascii(self):
        self.assertEqual(remove_vowels("zbcd"), "zbcd")

if __name__ == '__main__':
    unittest.main()
``` 

The script can be run directly to execute the test suite, and the function can be imported and used independently in other scripts as needed.