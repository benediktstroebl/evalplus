```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""

    # algorithm idea: 
    # find the longest palindrome starting from any position. 
    # Append to the other string reverse of a string prefix that comes before the palindrome. 
    # For longest palindrome found so far
    longest_palindrome = ''
    for char in string:
        if is_palindrome(char):
            longest_palindrome += char
        else:
            longest_palindrome = char + longest_palindrome[::-1]
            
    return longest_palindrome
```
The code defines two functions: is_palindrome checks if a given string is a palindrome and make_palindrome generates a palindrome from an input string.