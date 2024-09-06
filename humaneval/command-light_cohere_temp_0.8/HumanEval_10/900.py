```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    # Find the longest palindrome suffix
    palindrome_suffix = find_longest_palindrome_suffix(string)

    # Append the reverse of the prefix to the suffix
    return palindrome_suffix + string[::-1]

def find_longest_palindrome_suffix(string):
    # Initialize the length of the longest palindrome as 0
    l = 0

    # Keep looping until the start of the string is reached
    while string[l] != ' ':
        # Find the first occurrence of a palindrome
        r = l
        while r < len(string) and string[r] == string[r][::-1]:
            r += 1
        l = r

    return string[l:].replace('', '')
```
This code solves the problem of finding the shortest palindrome using the concept of longest palindrome suffix.  The all:
1. Palindrome is just of the first letter
2. The sum of the number of characters that come before the first occurrence of a palindrome is the length of the longest palindrome.