```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""

    palindrome = ""
    for char in string:
        if char == palindrome[-1] or char == palindrome[-2]:
            palindrome += char
        else:
            palindrome = palindrome[:-len(palindrome)] + char

    return palindrome[::-1]
```
The `make_palindrome` function uses a simple algorithm to create the shortest palindrome from a given string. The `is_palindrome` function checks if a given string is a palindrome by comparing it with its reverse. 
You can add more test cases and adjustments to these functions to fulfill more problem requirements.