Here's a Python script with a self-contained function that solves the problem of checking if a given text is a palindrome:
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.
    """
    # Convert string to lowercase and remove all non-alphanumeric characters
    text = ''.join(c for c in text if c.isalnum()).lower()
    
    # Check if the reversed text matches the original text
    return text == text[::-1]
```
This script defines a function 'is_palindrome' that takes a string text as an argument and returns True if it is a palindrome (reads the same forwards and backwards) and False otherwise. The function first cleans the input text by converting it to lowercase and removing all non-alphanumeric characters using a list comprehension. Then it compares the cleaned string with its reverse using slicing to determine if it's a palindrome.

Here's how we can test this function using Python's built-in `unittest` module:
```python
import unittest

def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.
    """
    # Convert string to lowercase and remove all non-alphanumeric characters
    text = ''.join(c for c in text if c.isalnum()).lower()
    
    # Check if the reversed text matches the original text
    return text == text[::-1]

class TestIsPalindrome(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(is_palindrome(''))

    def test_palindrome_strings(self):
        self.assertTrue(is_palindrome('aba'))
        self.assertTrue(is_palindrome('aaaaa'))

    def test_non_palindrome_strings(self):
        self.assertFalse(is_palindrome('zbcd'))
        self.assertFalse(is_palindrome('abcde'))

    def test_mixed_strings(self):
        self.assertTrue(is_palindrome('Racecar')) 
        self.assertFalse(is_palindrome('Hello')) 

if __name__ == '__main__':
    unittest.main()
```
In this test suite, we have several test cases, including testing with empty strings, palindrome strings, and non-palindrome strings, ensuring the function 'is_palindrome' works correctly for all cases. 
The `unittest.main()` function is used to discover and run the tests within the module.