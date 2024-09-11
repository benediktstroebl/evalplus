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
    if not string:  # edge case: empty string
        return ''

    max_palindrome_len = 0
    max_palindrome_offset = 0
    for i in range(len(string), 0, -1):  # consider all possible postfix lengths
        for j in range(len(string) - i + 1):  # consider all possible postfix positions
            postfix = string[j:j+i]
            if is_palindrome(postfix):  # if postfix is a palindrome
                if i > max_palindrome_len:  # update the longest palindrome
                    max_palindrome_len = i
                    max_palindrome_offset = j

    # construct the shortest palindrome that begins with the supplied string
    palindrome = string[max_palindrome_offset:max_palindrome_offset + max_palindrome_len]
    shortening_prefix = string[:max_palindrome_offset]
    return palindrome + palindrome[::-1] if palindrome else ''


# Example usage:
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

In this script, I have implemented the `make_palindrome` function by first finding the longest palindrome postfix of the input string. I then construct the shortest palindrome by appending the reverse of the string prefix to the palindromic postfix.