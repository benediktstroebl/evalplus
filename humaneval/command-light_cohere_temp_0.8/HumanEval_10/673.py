```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ''

    palindrome = ''
    while True:
        Palindrome_start = -1
        reverse_start = 0
        length = len(string)

        # Find the index of the longest palindrome suffix
        for i in range(length):
            if string[i] == string[::-1][i]:
                Palindrome_start = i
                break
            if i > reverse_start:
                reverse_start = i

        if Palindrome_start == -1:
            break

        # Append to the string the reverse of the prefix
        palindrome += string[:Palindrome_start] + string[::-1][reverse_start:]

    return palindrome
```