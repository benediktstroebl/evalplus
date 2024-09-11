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
    if not string:  # empty string is a palindrome
        return string

    longest_palindrome = ''
    for i in range(len(string), -1, -1):  # start from the longest possible palindrome
        for j in range(i):
            postfix = string[j:i]
            if is_palindrome(postfix):
                prefix = string[:j]
                palindrome = postfix + postfix[::-1]
                if len(palindrome) < len(longest_palindrome) + len(postfix):
                    longest_palindrome = postfix
                else:
                    longest_palindrome = prefix + palindrome
                break
        else:
            continue
        break

    return string + longest_palindrome


# Test cases
print(make_palindrome(""))  # ''
print(make_palindrome("cat"))  # 'catac'
print(make_palindrome("cata"))  # 'catac'
```
This script defines two functions: `is_palindrome` to check if a string is a palindrome and `make_palindrome` to find the shortest palindrome that begins with a supplied string. The `make_palindrome` function works by iterating over all possible postfixes of the input string in reverse order, checking if each is a palindrome, and then appending the reverse of the prefix to create a palindrome. If a longer palindrome is found, it replaces the current one. The function returns the shortest palindrome that begins with the input string.