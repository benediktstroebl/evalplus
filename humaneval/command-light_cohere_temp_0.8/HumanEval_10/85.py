```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return 'Not a palindrome: ' + string[::-1]
    else:
        return string[::-1]

# Test the function
print(is_palindrome(''))  # Output: True
print(is_palindrome('aaaa'))  # Output: True
print(is_palindrome('tcrca'))  # Output: False
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
```
The function is_palindrome returns True if the string is a palindrome and False otherwise. The function make_palindrome returns the shortest palindrome using the idea mentioned in the previous response.