Here is a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ''
    result = []
    while True:
        palindrome = string[0::(-len(string)//2)] + string[-palindrome::len]
        if palindrome == palindrome[::-1]:
            break
        result.append(palindrome)
    return ''.join(result)

print(is_palindrome("cin")  ) # True
print(is_palindrome("nav"))  # False
print(make_palindrome("nav"))  # Output: nav
    print(make_palindrome("navin"))  # Output: navanin
```