I have provided a self-contained Python function that solves the problem of finding the shortest palindrome using the given input string. The code is below demonstrates the implementation. 

```python
def is_palindrome(string): 
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string): 
    """ Find the shortest palindrome that begins with a supplied string """
    if not string: 
        return ""
    if len(string) <= 2: 
        return string
    prefix = string[: len(string) // 2]
    suffix = string[-len(string) // 2:]
    return prefix + suffix[::-1]
```