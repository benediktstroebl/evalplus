```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    palindrome = []
    while True:
        if is_palindrome(string[-1:]):
            palindrome.append(string[1:])
            break
        else:
            palindrome.append(string[::-1])

    return ''.join(palindrome)

# Test cases
print(make_palindrome(''))
print(make_palindrome('cat'))
print(make_palindrome('cata'))
print(make_palindrome('racecar'))
print(make_palindrome('hello'))
print(make_palindrome('python'))
```
The function is_palindrome checks if a given string is a palindrome, and the make_palindrome function creates a palindrome using the above algorithm.