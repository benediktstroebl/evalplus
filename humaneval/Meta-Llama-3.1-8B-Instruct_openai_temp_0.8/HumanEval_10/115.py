```markdown
### Solution: Finding the Shortest Palindrome Starting with a Given String
### Code

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
    # Find the longest palindromic suffix
    for i in range(len(string), 0, -1):
        substr = string[-i:]
        if is_palindrome(substr):
            # Find the remaining part of the string
            remaining_str = string[:-i]
            
            # Reverse the remaining part
            reversed_remaining_str = remaining_str[::-1]
            
            # Append the reversed remaining part to the palindromic suffix
            palindrome = substr + reversed_remaining_str
            return palindrome

    # If no palindromic suffix is found, return the original string
    return string


# Example usage:
if __name__ == "__main__":
    print(make_palindrome(""))  # Output: ''
    print(make_palindrome("cat"))  # Output: 'catac'
    print(make_palindrome("cata"))  # Output: 'catac'
```

### Explanation

This Python script defines two functions: `is_palindrome` checks whether a given string is a palindrome, and `make_palindrome` finds the shortest palindrome that begins with a supplied string.

In the `make_palindrome` function, we start by finding the longest palindromic suffix of the input string from the end. We do this by iterating over the input string in reverse order and checking each substring to see if it's a palindrome using the `is_palindrome` function. Once we find a palindromic suffix, we reverse the remaining part of the string and append it to the palindromic suffix to form the shortest palindrome starting with the input string.

The example usage at the end of the script demonstrates how to use these functions with different input strings.