```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''.join_with(string.split(''), lambda x: x+'r'*len(x)[::-1])

def not_palindrome(string):
    return 'Yes, ' + is_palindrome(string) + '! Yes! '

print(make_palindrome('cat')) # Output: catac
print(make_palindrome('cata')) # Output: catac
print(make_palindrome('abc')) # Output: abc 

print(is_palindrome('cat')) # Output: True
print(is_palindrome('cata')) # Output: False
print(is_palindrome('emery')) # Output: True
```