### Solution

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
    if not string:
        return string  # return empty string for empty input

    i = len(string) - 1  # initialize pointer at the end of the string
    for _ in range(len(string)):  # loop through the string backwards
        if string[i]!= string[0]:  # check if characters at the current position and beginning of the string are equal
            i -= 1  # if not, move the pointer to the left
        else:
            break  # if they are equal, break the loop

    return string + string[:i][::-1]  # return the original string with palindrome suffix


# Example usage:
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

### Explanation

The `make_palindrome` function takes a string as input and returns the shortest palindrome that begins with the supplied string.

Here's a step-by-step breakdown of the algorithm:

1.  If the input string is empty, return an empty string.
2.  Initialize a pointer `i` at the end of the string.
3.  Loop through the string backwards, checking if the character at the current position `i` is equal to the character at the beginning of the string. If they are not equal, move the pointer to the left.
4.  Once the pointer reaches the position where the characters at the current position and beginning of the string are equal, break the loop.
5.  Return the original string with the reverse of the prefix (before the palindromic suffix) appended to the end.

This solution has a time complexity of O(n), where n is the length of the input string, and a space complexity of O(n) for the reverse operation.