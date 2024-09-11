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
    # Check if string is already a palindrome
    if is_palindrome(string):
        return string

    # Find the longest palindrome suffix of string
    for i in range(len(string), 0, -1):
        suffix = string[-i:]
        if is_palindrome(suffix):
            # Find the longest prefix of the suffix's prefix that is a palindrome
            prefix = ''
            for j in range(len(suffix), 0, -1):
                prefix = suffix[:-j] + prefix
                if is_palindrome(prefix):
                    # Answer is formed by string prepended by reverse of prefix
                    return string + prefix[::-1]

# Test cases
import unittest
class TestPalindrome(unittest.TestCase):
    def test_make_palindrome(self):
        self.assertEqual(make_palindrome(''), '')
        self.assertEqual(make_palindrome('cat'), 'catac')
        self.assertEqual(make_palindrome('cata'), 'catac')
        self.assertEqual(make_palindrome('abba'), 'abba')

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome('abba'))
        self.assertFalse(is_palindrome('abc'))

if __name__ == '__main__':
    unittest.main()
```

This script includes the functions you requested, along with some test cases to ensure their correctness. The `make_palindrome` function searches through the string for the longest palindrome suffix, then finds the longest palindrome prefix of that suffix and appends the reverse of that prefix to the string.