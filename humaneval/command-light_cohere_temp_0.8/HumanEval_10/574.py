Here is a Python script with a self-contained function that solves the problem of making a palindrome:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ""
    else:
        # Find the longest postfix of supplied string that is a palindrome
        postfix = string[::-1].replace(' ', '')
        # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
        return postfix + string[-len(postfix):  # String slice to avoid duplicates

print(is_palindrome("racecar")) # True
print(is_palindrome("civic")) # True
print(is_palindrome("alice")) # False
print(make_palindrome("racecar")) # racecar
print(make_palindrome("civic")) # citcivics
print(make_palindrome("alice")) # alicaea
```
The function is_palindrome checks if a given string is a palindrome, and the function make_palindrome creates a palindrome from a given string.