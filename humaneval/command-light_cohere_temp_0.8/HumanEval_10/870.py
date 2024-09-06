The solution and tests are all wrapped into a single function.

Let's take a look at the code:
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string """
    
    # Algorithm idea:
    # Find the longest postfix of supplied string that is a palindrome
    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    return ''.join(prefix + suffix for prefix, suffix in zip(''.reverse(string[:-len(string) - 1])) + string[-1:]
```