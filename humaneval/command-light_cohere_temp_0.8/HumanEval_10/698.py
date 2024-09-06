The function `make_palindrome` takes a string as input and generates the shortest palindrome using the provided algorithm:

```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string
    Algorithm idea:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to theend of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    lengthy postfix:
    - append reversed palindrome
    - find new longest postfix
    - repeat until the full string is palindromic.
    """
    string = ''
    while not is_palindrome(string):
        postfix = string[-1]
        prefix = string[:-len(postfix)]
        string = prefix + postfix + string
    return string
```

This approach follows the algorithm to find the shortest palindrome using the idea of breaking the string into a prefix and a suffix and then concatenating them in reverse order to get the palindrome.