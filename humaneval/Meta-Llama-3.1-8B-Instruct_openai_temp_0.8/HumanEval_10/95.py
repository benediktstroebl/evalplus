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
    while True:
        # Check if the string is already a palindrome
        if is_palindrome(string):
            return string
        # Find the longest suffix that is a palindrome
        for i in range(len(string), 0, -1):
            suffix = string[-i:]
            if is_palindrome(suffix):
                # Reverse the prefix and append to the palindromic suffix
                prefix = string[:-i]
                string = prefix + suffix + prefix[::-1]
                break


import unittest

class TestMakePalindrome(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(make_palindrome(''), '')

    def test_single_character(self):
        self.assertEqual(make_palindrome('a'), 'a')

    def test_already_palindrome(self):
        self.assertEqual(make_palindrome('catac'), 'catac')

    def test_simple_example(self):
        self.assertEqual(make_palindrome('cat'), 'catac')

if __name__ == '__main__':
    unittest.main()
```

This script contains the `make_palindrome` function which generates a palindrome by finding the longest postfix that is a palindrome, and appending the reverse of the prefix to it. It also includes unit tests to ensure the function behaves correctly.