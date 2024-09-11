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
    def is_suffix_palindrome(s: str, i: int) -> bool:
        """ Check if a suffix of the string `s` is a palindrome starting at index `i`. """
        return s[:i+1] == s[:i+1][::-1]

    # Find the longest postfix of supplied string that is a palindrome
    for i in range(len(string), -1, -1):
        if is_suffix_palindrome(string, i):
            break

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    prefix = string[:i]
    suffix = string[i:]
    return string + prefix[::-1]


# Test cases
import unittest

class TestMakePalindrome(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(make_palindrome(''), '')

    def test_single_character(self):
        self.assertEqual(make_palindrome('a'), 'a')

    def test_even_length(self):
        self.assertEqual(make_palindrome('cata'), 'catac')

    def test_odd_length(self):
        self.assertEqual(make_palindrome('cat'), 'catac')

if __name__ == '__main__':
    unittest.main(argv=[__file__])
```

This script contains the `is_palindrome` and `make_palindrome` functions as specified, along with some test cases to verify their correctness.