```python
def is_palindrome(string): 
    return string == string[::-1]

def make_palindrome(string): 
    if not_palindrome(string):
        return string + string[::-1]
    else:
        return ''.join([char for c if c.isalnum() andpalindrome(string) else c for c in string])
```
The function is_palindrome checks if a given string is a palindrome or not, by comparing the original string with its reverse. The function make_palindrome finds the shortest palindrome that begins with the given string by iterating through each character and checking if it is a palindrome or not. If the function finds a palindrome, it returns the full palindrome, otherwise, it returns an empty string.