Here is a Python script that contains a self-contained function to solve the problem of finding the shortest palindrome:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    # Finds the shortest palindrome that begins with a supplied string.
    # Algorithm idea: 
    # 1. Find the longest postfix of supplied string that is a palindrome.
    # 2. Append to the string reverse of a string prefix that comes before the palindromic suffix.
    return ''.join(string + string[::-1])
```
The function is_palindrome checks if a given string is a palindrome. The function make_palindrome creates a new string by concatenating the reversed version of the original string with its reverse. 

It does this by using the join function along with string slicing.