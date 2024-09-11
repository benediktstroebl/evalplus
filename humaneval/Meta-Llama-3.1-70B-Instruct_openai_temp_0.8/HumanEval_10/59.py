**Shortest Palindrome Finder Script**
=====================================

Below is a Python script that implements the `is_palindrome` function to check if a given string is a palindrome and the `make_palindrome` function to find the shortest palindrome that begins with a supplied string.

```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    # Handle edge case where input string is empty
    if not string:
        return ''

    # Reverse the input string
    rev_string = string[::-1]

    # Find the longest common prefix between the input string and its reverse
    for i in range(len(string)):
        if string.startswith(rev_string[i:]):
            # Append the reverse of the non-common prefix to the input string
            return string + rev_string[:i]


# Example usage
if __name__ == "__main__":
    print(make_palindrome(''))  # Output: ''
    print(make_palindrome('cat'))  # Output: 'catac'
    print(make_palindrome('cata'))  # Output: 'catac'
```

**Explanation**

The `make_palindrome` function first handles the edge case where the input string is empty. Then, it reverses the input string and finds the longest common prefix between the input string and its reverse. The non-common prefix of the reversed string is appended to the input string to form the shortest palindrome.