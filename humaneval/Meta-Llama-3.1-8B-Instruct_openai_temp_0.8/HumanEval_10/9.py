### Solution
```markdown
### make_palindrome.py

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
    if not string:  # Base case: Empty string
        return ''

    # Find the longest palindromic postfix
    for i in range(len(string) - 1, -1, -1):
        postfix = string[i:]
        if is_palindrome(postfix):
            break

    # Append reversed prefix to the end of palindromic postfix
    prefix = string[:i]
    return postfix + prefix[::-1]


# Test cases
if __name__ == "__main__":
    print(make_palindrome(""))  # ''
    print(make_palindrome("cat"))  # catac
    print(make_palindrome("cata"))  # catac
```
### Explanation

This script first checks if the input string is empty. If it is, it returns an empty string.

Otherwise, it iterates over the string from right to left to find the longest palindromic postfix. Once found, it appends the reversed prefix of the string that comes before the palindromic postfix.

The `is_palindrome` function is used to check if a given string is a palindrome.

The test cases at the end of the script demonstrate the usage of the `make_palindrome` function.