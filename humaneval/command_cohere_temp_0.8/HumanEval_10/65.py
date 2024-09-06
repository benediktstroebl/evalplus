Here's a Python script with a self-contained function that solves the problem of constructing the shortest palindrome that begins with a supplied string, and supplements it with corresponding tests:

```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return string
    
    # Find the longest palindromic suffix
    i = string.rfind('.{}'.format(string[::-1]))
    if i == -1:
        return string
    
    return string[:i] + make_palindrome(string = string[i+1:]) + string[i+1:i][::-1]

# Test cases
assert is_palindrome('')
assert is_palindrome('foo')
assert not is_palindrome('fooobarc')

assert make_palindrome('') == ''
assert make_palindrome('foo') == 'foo'
assert make_palindrome('fooobarc') == 'fooobarc'
assert make_palindrome('cata') == 'catac'
assert make_palindrome('aaa') == 'aaa'
```

This script defines a function `make_palindrome` that takes a string as input and constructs the shortest palindrome possible that begins with the input string. The function uses a simple algorithm that recursively constructs the palindrome by finding the longest palindromic suffix of the evolving string and then trimming and reversing the non-palindromic prefix.

The script also includes test cases that validate the behavior of both the `is_palindrome` and `make_palindrome` functions. 

Run the script to test out the functions!