```python
def is_palindrome(string):
    """Test if given string is a palindrome"""
    return string == string[::-1]

def make_palindrome(string):
    """Find the shortest palindrome that begins with a supplied string"""
    if not string:
        return ""
    
    palindrome = ""
    while True:
        palindrome = palindrome + string[0] + string[-1:]
        if is_palindrome(palindrome):
            break
    return palindrome
```
The function is_palindrome checks if a given string is a palindrome or not. The function make_palindrome finds the shortest palindrome that begins with a given string. The function works by first appending the first and last character of the string to create a palindrome. It then checks if the strings that form a palindrome are indeed palindromes. The algorithm works by using a simple brute force method to find the shortest palindrome.