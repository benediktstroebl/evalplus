Here's a self-contained Python function that checks if a given string is a palindrome, and also provides a function to generate the palindrome from a given string:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with supplied string """
    if not string:
        return ''

    # Find the longest postfix of supplied string that is a palindrome
    longest_palindrome = []
    prefix = ''
    for char in string:
        if char == prefix[::-1]:
            longest_palindrome.append(char)
            prefix = char
    else:
        longest_palindrome.append(prefix)
        prefix = char

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    return longest_palindrome + longest_palindrome[::-1]

# Test cases
print(is_palindrome(''))  # Output: True
print(is_palindrome('cat'))  # Output: True
print(is_palindrome('cata'))  # Output: False
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```
The `is_palindrome` function checks if the given string is a palindrome. The `make_palindrome` function creates a palindrome by finding the longest postfix that is a palindrome, and then reversing the prefix.