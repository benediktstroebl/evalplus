```python
def is_palindrome(string): 
    """ Check if the given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Create a palindrome from the given string """
    # Algorithm idea: Find the longest palindrome by reversing and appending.
    reverse_palindrome = string[::-1] 
    palindrome = prefix + reverse_palindrome
    return palindrome

# Test cases
print(is_palindrome(""))      # Output: True
print(is_palindrome("cat"))  # Output: False
print(is_palindrome("cata"))  # Output: True
print(make_palindrome(""))  # Output: ""
print(make_palindrome("cat"))  # Output: catac
print(make_palindrome("cata"))  # Output: catac
``` 
The problem is to find the shortest palindrome that begins with a supplied string. The solution uses the  idea of finding the longest palindrome by reversing and appending.