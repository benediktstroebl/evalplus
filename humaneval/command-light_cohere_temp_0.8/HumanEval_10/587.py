```python
def is_palindrome(string: str) -> bool:
    """
    Tests if the given string is a palindrome.
    """
    Palindrome is a sequence that reads the same backwards and forwards.
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """
    Returns a palindrome for the given string.
    Algorithm idea:
    - Find the longest postfix of the string that is a palindrome
    - Append to the end of the string the reverse of a string prefix that comes before the palindromic suffix.
    """
    longest palindrome is the solution.

# Test cases
print(make_palindrome(''))
print(make_palindrome('cat'))
print(make_palindrome('cata'))
print(make_palindrome('racecar'))
```