```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''.join_palindrome(string)
    return ''.join_palindrome(string)[::-1]

def join_palindromes(string):
    if not_palindrome(string):
        return ''
    return ''.join_palindrome(string[:-len(string)//2]) + join_palindromes(''.join_palindrome(string[::len(string)//2:])

def not_palindrome(string):
    return bool(is_palindrome(string))

print(make_palindrome(''))
print(make_palindrome('cat'))
print(make_palindrome('cata'))
print(join_palindromes('abc'))
print(join_palindromes('cad'))
```
The solution uses the palindrome property of strings, where the same sequence of characters appears both forwards and backwards. This function is generating the string is a palindrome. The idea is to reverse the prefix and append the reversed prefix to the end of the original string to make it a palindrome.