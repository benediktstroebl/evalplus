Here's a self-contained Python function that solves the problem of creating a palindrome:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string.
    palindromes = [a for a in string if is_palindrome(a)] 
    return palindromes and string[::-1] == palindromes
```

The code defines two functions: is_palindrome checks if a given string is a palindrome, and make_palindrome creates a palindrome given a string. 

The is_palindrome function follows a simple pattern where it checks if the string and its reverse are the same. The make_palindrome function uses the is_palindrome function to filter out all the palindromic characters from the string and then reverses them.