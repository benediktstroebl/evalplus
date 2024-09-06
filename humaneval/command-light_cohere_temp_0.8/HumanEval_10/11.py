Here is a self-contained Python script that solves the problem of making a palindrome of a given string:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return string + string[::-1]
    return make_palindrome(string[1:])

def not_palindrome(string):
    return ''.join(make_palindrome(char) for char in string if is_palindrome(char))
```
The code defines three functions:
1. `is_palindrome` — checks if a given string is a palindrome by comparing it with its reverse.
2. `make_palindrome` finds the palindrome by checking if the string is not a palindrome and then recursively constructs a palindrome by appending the reverse of the first half of the string.
3. `palindrome` uses the method is the same as the above one, but uses slicing to remove the first character from the string.

In summary, this code provides a self-contained solution to the problem of making a palindrome from a given string.