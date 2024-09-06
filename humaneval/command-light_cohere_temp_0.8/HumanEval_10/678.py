Here's the solution:
```Python
def is_palindrome(string): 
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    palindrome = string[:0:len(string)//2]
    return palindrome + palindrome[::-1]
```
The `make_palindrome` function uses the `is_palindrome` helper function to efficiently determine if the input string is already a palindrome and, if not, constructs and returns the shortest palindromic version of the string.