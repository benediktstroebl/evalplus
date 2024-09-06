```python
def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.
    """
    # Split the string into individual characters and reverse the list.
    char_list = list(text)
    reversed_char_list = char_list[::-1]
    
    # Compare the characters character-wise to check if it's a palindrome.
    return text == ''.join(reversed_char_list)
```

This function splits the input string into individual characters and then reverses the resultant list. Finally, it compares the reversed string with the original one character by character to determine if it's a palindrome. This approach ensures a time complexity of `O(n)` where `n` is the length of the input string.

Here's how you could test this function using Python's `unittest` framework:
```python
import unittest

def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.
    """
    # Split the string into individual characters and reverse the list.
    char_list = list(text)
    reversed_char_list = char_list[::-1]
    
    # Compare the characters character-wise to check if it's a palindrome.
    return text == ''.join(reversed_char_list)

class TestIsPalindrome(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(is_palindrome(''))

    def test_palindrome_strings(self):
        self.assertTrue(is_palindrome('aba'))
        self.assertTrue(is_palindrome('aaaaa'))

    def test_non_palindrome_strings(self):
        self.assertFalse(is_palindrome('zbcd'))

    def test_strings_with_whitespaces(self):
        self.assertFalse(is_palindrome('a ab'))

    def test_single_character(self):
        self.assertTrue(is_palindrome('a'))

if __name__ == '__main__':
    unittest.main()
```

This test suite includes tests for different scenarios, such as empty strings, palindromic strings, non-palindromic strings, strings with whitespace, and single-character strings. Running the suite via `unittest.main()` will execute each test case, providing you with clear feedback on whether the `is_palindrome` function is correctly implemented.