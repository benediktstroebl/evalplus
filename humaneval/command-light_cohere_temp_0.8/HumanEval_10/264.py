```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''
    else:
        return ''.join(string[i:][::-1] for i in range(0, len(string)-1))

print(is_palindrome(""))
print(is_palindrome("racecar"))
print(is_palindrome("hello"))
print(make_palindrome(""))
print(make_palindrome("Hello"))
print(make_palindrome("racecar")))
```
The code defines two functions: `is_palindrome` checks if a given string is a palindrome or not, and `make_palindrome` creates a palindrome from a given string.  The `make_palindrome` function uses a simple algorithm to find the shortest palindrome. It first checks if the`make_palindrome` returns an empty string for an empty string, and for a string with no palindrome, it appends the reversed characters of the string to create a palindrome.