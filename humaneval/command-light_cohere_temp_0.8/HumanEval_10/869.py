Here is a self-contained Python script with a function that solves the problem of creating a palindrome from a given string:
```python
def is_palindrome(string):
    return string == string[::-1] # returns boolean

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string.
    Palindrome = [string[0:1] + string[1:][::-1]
    return palindrome

print(is_palindrome("")) # returns True
print(is_palindrome("hello")) # returns True
print(make_palindrome("")) # returns ""
print(make_palindrome("world")) # returns "worldw"
print(make_palindrome("hello world")) # returns "ohellu"
```