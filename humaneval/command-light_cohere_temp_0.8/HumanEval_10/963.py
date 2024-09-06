Here's the solution:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    # Find the longest palindrome
    palindrome = []
    for char in string:
        if char == palindrome[-1] or palindrome[-1] == char:
            palindrome.append(char)
        else:
            palindrome.append(char)
            # Reverse the string to the beginning and append the palindrome to the end
    return ''.join.join(reversed(palindrome))
```
The function 'make_palindrome' takes a string as input and finds the longest palindrome that begins with the supplied string. Then, it reverses the string and appends the palindrome to the end. In other words, it finds the longest palindrome and returns its reversed string.