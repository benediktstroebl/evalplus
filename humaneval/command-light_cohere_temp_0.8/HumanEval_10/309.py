Here is a self-contained Python function that solves the problem you have described: 

```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""
    else:
        return "".join(reversed(string) + reversed(reversed(string)))

def not_palindrome(string):
    return is_palindrome(make_palindrome(string))

# Example usage:
# Test if function is_palindrome('')
# test if function is_palindrome('cat')
# test if function is_palindrome('cata')
``` 

This script defines two functions: is_palindrome checks if a given string is a palindrome, and make_palindrome creates a palindrome given a string. Both functions use a
 approach to create a palindrome string: