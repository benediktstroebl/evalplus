```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    # Reverse the input string to compare later
    rev_string = string[::-1]
    
    # Check all prefixes of the reversed string to find the common prefix with the original string
    for i in range(len(string)):
        prefix = string[:len(string) - i]
        suffix = string[-i:]
        if is_palindrome(suffix) and prefix == rev_string[:len(prefix)][::-1]:
            return string + suffix[::-1]
    
    # If no common prefix found, the original string is already a palindrome
    return string + string[::-1]


# Test cases
import unittest

class TestPalindromeFunctions(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome('radar'))
        self.assertFalse(is_palindrome('python'))

    def test_make_palindrome(self):
        self.assertEqual(make_palindrome(''), '')
        self.assertEqual(make_palindrome('cat'), 'catac')
        self.assertEqual(make_palindrome('cata'), 'catac')

if __name__ == '__main__':
    unittest.main()
```

In this code:

1. The `is_palindrome` function checks if a string is a palindrome by comparing it with its reverse.
2. The `make_palindrome` function finds the shortest palindrome that begins with a supplied string by appending the reverse of a string prefix that comes before the palindromic suffix to the original string.
3. Test cases are included using the `unittest` module to ensure the functions work correctly.
4. The `if __name__ == '__main__':` block runs the test cases when the script is executed directly (not when it's imported as a module).