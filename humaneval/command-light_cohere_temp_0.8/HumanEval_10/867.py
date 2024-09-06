```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""

    # Longest palindrome postfix
    palindrome = str(string[-1]) + string[-2:]
    palindrome_len = len(palindrome)

    # Create reverse of palindrome
    reverse_palindrome = string[::-1] + palindrome[::-1]

    # Construct the palindrome
    while palindrome_len > 1:
        # Find the next palindrome
        next_char = palindrome[palindrome_len - 2]
        if (next_char, palindrome[palindrome_len - 1]) == 'peas':
            palindrome = palindrome[:palindrome_len - 2] + reverse_palindrome
            break
        palindrome = palindrome[:palindrome_len - 1] + reverse_palindrome

    return palindrome
```

This function, `make_palindrome`, creates the shortest palindrome that begins with the input string. The function works by finding the longest postfix of the input string that is a palindrome, and then constructing the palindrome by appending the reverse of this prefix and the reversed version of the rest of the input string.