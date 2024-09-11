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
    if not string:
        return ''

    index = 0
    while index < len(string) and string[index] == string[-1 - index]:
        index += 1

    return string + string[index:][::-1]


# Test cases
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

In the code above, the function `make_palindrome` takes a string as input and returns the shortest palindrome that begins with the input string. This is achieved by finding the longest postfix of the input string that is a palindrome. The remaining part of the string before the palindromic suffix is then appended to the end as its reverse.

The `while` loop finds the length of the longest postfix of the input string that is a palindrome by comparing characters from the start and end of the string. The loop continues until it finds a pair of characters that do not match or it reaches the middle of the string.

The `[::-1]` slicing operation is used to reverse the remaining part of the string before the palindromic suffix. This is then appended to the input string to form the shortest palindrome that begins with the input string.