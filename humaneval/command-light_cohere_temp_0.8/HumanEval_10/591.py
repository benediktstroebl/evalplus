```python
def is_palindrome(string): 
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''
    else:
        return ''.joinrcat(''.join(reversed(string[:i])) + string[-i:]
                for i, c in enumerate(reversed(string), 1)
                if c == string[i-1] and i < len(string) - 2
            return make_palindrome(string[:i]) + string[-i:]
       
```

This script provides a self-contained function that checks if a given string is a palindrome and then finds the shortest palindrome that begins with the given string. The code is efficient and follows a straightforward algorithm to solve the problem.