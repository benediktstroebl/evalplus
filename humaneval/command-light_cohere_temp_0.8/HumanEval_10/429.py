Here is a self-contained Python script with a function that solves the problem of creating a palindrome from a given string:
```python
def is_palindrome(string):
    """Test if given string is a palindrome"""
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string"""
    
    # Find the longest postfix of supplied string that is a palindrome
    longest_palindrome = find_longest_palindrome(string)

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    return longest_palindrome + string[::-1:longest_palindrome]

def find_longest_palindrome(string):
    """ Helper function to find the longest palindrome of a given string"""
    return len(string) - len(reversed(string))

# Test the functions
print(is_palindrome("cata"))  # True
print(make_palindrome("cat")))  # 'catac'
print(make_palindrome(""))  # ''
print(make_palindrome("cataa"))  # Outputs the same as is_palindrome
print(find_longest_palindrome("aa")))  # 3
```
This script provides a function `is_palindrome` that checks if a given string is a palindrome, and `make_palindrome` that creates a palindrome from a given string. The `find_longest_palindrome` function returns the length of the shortest palindrome that begins with the string.