```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    palindrome = string[::-1] + string[:-len(string) // 2]
    return palindrome
```
The function is_palindrome checks if the input string is a palindrome. The function make_palindrome constructs a palindrome by first checking for an existing palindrome using is_palindrome and returning an empty string if not. If a palindrome is found, it concatenates the palindrome with the string prefix that comes before the palindromic suffix using slicing. 

This approach efficiently constructs the shortest palindrome.