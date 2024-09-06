```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""

    # Find the longest palindrome
    max_len = 0
    palindrome = ""
    for char in string:
        if is_palindrome(char) and len(palindrome) < max_len:
            palindrome = char
            max_len = 1
    return palindrome + palindrome[::-1]
```
The provided code defines two functions: `is_palindrome` checks if a given string is a palindrome and returns a boolean value, while `make_palindrome` creates a palindrome from a given string. The algorithm in `make_palindrome` starts by checking if the string is already a palindrome. If it is, the function returns the string as is. If not, it iterates through each character in the string. It keeps track of the longest palindrome found so far and appends it to the beginning of the string. Then, it reverses the string and appends the reverse of the palindrome found.