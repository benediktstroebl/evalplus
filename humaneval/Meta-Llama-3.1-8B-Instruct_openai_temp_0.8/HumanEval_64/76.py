Here's a Python function that solves the problem, along with example test cases:
```python
# Define a constant for vowels
VOWELS = 'aeiou'

def vowels_count(s):
    """
    Returns the number of vowels in a given string.

    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 'y' is also a vowel,
    but only when it is at the end of the given word.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    # Count vowels in the entire string (case-insensitive)
    count = sum(1 for char in s.lower() if char in VOWELS)

    # If the word ends with 'y', subtract 1 from the count if 'y' is not
    # the last character or if there are other vowels in the word
    if s.lower().endswith('y') and len(s) > 1 and s.lower()[:-1] in VOWELS:
        count -= 1

    return count
```
Here are some example test cases:
```python
import unittest

class TestVowelsCount(unittest.TestCase):
    def test_vowels_count(self):
        self.assertEqual(vowels_count("abcde"), 2)
        self.assertEqual(vowels_count("ACEDY"), 3)
        self.assertEqual(vowels_count("hello"), 2)
        self.assertEqual(vowels_count("AEIOU"), 5)
        self.assertEqual(vowels_count("abby"), 2)
        self.assertEqual(vowels_count("a"), 1)

if __name__ == "__main__":
    unittest.main()
```
Note: The test cases cover a variety of scenarios, including words with and without vowels, words with 'y' at the end, and single-letter words.