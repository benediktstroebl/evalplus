```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''
    else:
        return ''.join_reverse(string[:-len(string)//2]+string[-1:])

# Test if the function is correct
print(is_palindrome('')) # True
print(is_palindrome('c')) # True
print(is_palindrome('ca')) # True
print(is_palindrome(' backwards  ')) # False
print(make_palindrome('')) # ''
print(make_palindrome('cat')) # 'catac'
print(make_palindrome('cata')) # 'catac'
```
The code defines two functions: `is_palindrome` and `make_palindrome`. The `is_palindrome` function returns `True` if the input string is a palindrome, and `False` otherwise. The `make_palindrome` function constructs a palindrome using the `is_palindrome` function, initially checking if the input string is a palindrome.