A solution to the prompt is:

```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""
    palindrome = ""
    for char in string:
        if char == palindrome[-1] or is_palindrome(palindrome[-1:]):
            palindrome += char
        else:
            palindrome += char[::-1]
    return palindrome
```

Here, the code defines a function is_palindrome that checks if a given string is a palindrome. The function make_palindrome creates a new string that tries to be a palindrome. The function iterates over each character in the original string and appends them to the palindrome string if the character is a palindrome of the last character or its reverse, respectively. This algorithm tries to find the shortest palindrome.