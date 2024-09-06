Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

The function removes vowels from the input text using the `translate` method and provides tests that cover different scenarios. 
This approach leverages the `str.translate()` method and the `str.maketrans()` function to remove vowels from the text.

```python
# Test the remove_vowels function
import unittest

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))

class TestRemoveVowels(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_vowels(""), "")

    def test_strings_with_spaces(self):
        self.assertEqual(remove_vowels("abcdef ghijklm"), "bcdf ghjklm")

    def test_single_word(self):
        self.assertEqual(remove_vowels("abcdef"), "bcdf")

    def test_multiple_vowels(self):
        self.assertEqual(remove_vowels("aaaaa"), "")

    def test_vowels_at_beginning_and_end(self):
        self.assertEqual(remove_vowels("aaBAA"), "B")

    def test_special_characters(self):
        self.assertEqual(remove_vowels("zbcd"), "zbcd")

if __name__ == '__main__':
    unittest.main()
```

This test suite includes several test functions that cover different scenarios of the `remove_vowels` function, ensuring its correctness and robustness in various cases.