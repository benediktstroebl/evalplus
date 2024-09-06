Here's the solution to the Palindrome Generator problem:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return string + string[::-1]
    return make_palindrome(string[1:])

def not_palindrome(string):
    return is_palindrome(string) and make_palindrome(string) == string
```
The `make_palindrome` function follows a simple recursive approach. It begins by looking for the string prefix that is also a palindrome. If such a river, it reverses the prefix and appends it to the string, producing a palindrome. Otherwise, it recursively calls itself with the substring from the beginning of the string.

This approach is effective because it requires less memory to operate and is capable of solving larger strings. The code also has a self-contained property, which means that it may be used to create a palindrome for any given string.