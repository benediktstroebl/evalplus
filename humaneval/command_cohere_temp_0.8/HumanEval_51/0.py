Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

The function removes vowels from the input text using the `translate` method and provides tests that cover various scenarios such as an empty string, different text cases, and varying vowel contents in the input text.

You can execute this code to see the complete implementation along with the tests:
```python
import unittest

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))

class TestRemoveVowels(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(remove_vowels(""), "")

    def test_single_word(self):
        self.assertEqual(remove_vowels("aaaaa"), "")
        self.assertEqual(remove_vowels("aaBAA"), "B")

    def test_multiple_words(self):
        self.assertEqual(remove_vowels("abcdef"), "bcdf")
        self.assertEqual(remove_vowels("abcdef\nghijklm"), "bcdf\nghjklm")

    def test_non_letters(self):
        self.assertEqual(remove_vowels("zbcd"), "zbcd")

if __name__ == '__main__':
    unittest.main()
```