A solution for the problem is:
```python
def is_palindrome(string): 
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    lis = [char for char in string if char == string[1:]
    lis.append(string[0])

    palindrome = lis[::-1] + lis[1:]
    return palindrome
```
The function 'make_palindrome' generates the shortest palindrome from a given string. It uses the simple method of finding the longest palindrome suffix and prepends it to the prefix to create the palindrome.