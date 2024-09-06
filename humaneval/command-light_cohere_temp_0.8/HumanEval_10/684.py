```python
def is_palindrome(string: str) -> bool:
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    if not_palindrome(string):
        return 'error: cannot make palindrome'

    return make_palindrome_helper(string, str. after_palindrome)

def make_palindrome_helper(string: str, prefix: str) -> str:
    if prefix == string[-1]:  # Check if the string already ends with a palindrome or prefix
        return string
    
    # Find the longest postfix of a palindrome in the string
    palindrome_part = [i for i, char in enumerate(string) if char == prefix[0]]
    if not palindrome_part:
        return string + prefix[1:]  # No palindrome, add prefix to the end
    else:
        return prefix + palindrome_part[-1]  # Return the palindrome

# Test
print(make_palindrome('cat'))  # Output: catac
print(make_palindrome('cata'))  # Output: catac
print(make_palindrome('car'))   # Output: carroa
```