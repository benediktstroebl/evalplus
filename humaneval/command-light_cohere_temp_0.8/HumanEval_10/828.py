```python
def is_palindrome(string: str) -> bool:
    """
    Tests if the given string is a palindrome or not.
    """
    returns True if the string is a palindrome, else False.
"""#palindrome("") # True
#palindrome("") # False
def make_palindrome(string: str) -> str:
    """
    Finds the shortest palindrome that begins with a supplied string.
    Algorithm idea simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    reverse = string[::-1]
    # Append the reverse to the beginning of the string
    #longest_palindrome = reverse[::-1] + string[:-len(reverse)]
    longest_palindrome = reverse + string[:-len(reverse)]
    return longest_palindrome
```