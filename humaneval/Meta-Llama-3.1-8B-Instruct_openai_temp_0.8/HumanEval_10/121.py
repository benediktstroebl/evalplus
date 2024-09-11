### Code Generation

The following Python script completes the problem by filling in the implementation of the `make_palindrome` function.

```markdown
### Problem Solution
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with a supplied string.

    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.

    Args:
        string (str): The input string.

    Returns:
        str: The shortest palindrome that begins with the input string.

    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    while not is_palindrome(string):
        # Find the longest suffix that is a palindrome
        suffix = ''
        for i in range(len(string), 0, -1):
            suffix = string[:i]
            if is_palindrome(suffix):
                break

        # Append the reverse prefix
        prefix = string[:len(string) - len(suffix)]
        string = suffix + prefix[::-1]
    return string


# Example use cases
if __name__ == "__main__":
    print(make_palindrome(""))
    print(make_palindrome("cat"))
    print(make_palindrome("cata"))
```

### Explanation

The `make_palindrome` function finds the shortest palindrome starting with the input string. It repeatedly finds the longest suffix of the input string that is a palindrome and appends the reverse of the prefix that comes before this palindromic suffix.

We achieve this by utilizing a while loop that continues until the input string is a palindrome. Inside the loop, we find the longest suffix that is a palindrome, and append the reverse of the prefix that comes before this palindromic suffix to the input string.

Finally, we return the modified string, which is now the shortest palindrome that begins with the input string.

The `is_palindrome` function remains unchanged and serves as a helper function to check whether a given string is a palindrome.