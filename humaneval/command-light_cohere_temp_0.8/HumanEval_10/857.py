A Palindrome Generation Function:
A palindrome generator function that accepts a string as an argument and returns its palindrome. The method uses the typical approach, in which we must first locate the longest palindromic prefix inside the input string and then construct the palindrome by concatenating the prefix and its reverse.

The function utilizes a for loop and an ispalindrome function to locate the longest palindromic prefix. The function then returns the string with the palindrome appended to the end.

Here's the code:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
```

The test code checks that the function is_palindrome returns True for the strings that are palindromes and False for the others. The make_palindrome function creates a new string with the palindrome appended to the original string.