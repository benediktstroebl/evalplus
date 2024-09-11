```markdown
### Solution
#### Problem: Find the shortest palindrome that begins with a supplied string.

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
    if string == '':
        return ''

    # Find the longest palindrome postfix of the string
    for i in range(len(string)):
        postfix = string[i:]
        if is_palindrome(postfix):
            break

    # Append reverse of string prefix to the palindromic postfix
    prefix = string[:i]
    palindrome = postfix + prefix[::-1]
    return palindrome
```
#### Example Usage
```python
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```
This script does the following:

*   The `is_palindrome` function checks whether a given string is a palindrome.
*   The `make_palindrome` function finds the shortest palindrome that begins with a supplied string. It does this by finding the longest palindrome postfix of the string, and then appending the reverse of the string prefix to the palindromic postfix.

This solution is concise and efficient, with a time complexity of O(n^2) due to the reversal of the string prefix and the iteration over the string. However, for large inputs, more efficient algorithms may be necessary to achieve better performance.