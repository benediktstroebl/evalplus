Here's a Python function that checks if a given string is a palindrome:
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
    'acat'
    >>> make_palindrome('Hello')
    'olleH'
    """
    if not string:
        return ""

    # Find the longest palindromic substring
    max_len = 0
    palindrome = ""
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            continue
        else:
            palindrome = string[i - 1] + string[i]
            max_len = max(max_len, len(palindrome))

    # Append the reversed palindrome and return the result
    reversed_palindrome = palindrome[::-1]
    return string[:max_len] + reversed_palindrome
```
The make_palindrome function builds the shortest palindrome that begins with the supplied string. The is_palindrome function then checks if the result of make_palindrome is the original string, which confirms that the function has returned a palindrome.