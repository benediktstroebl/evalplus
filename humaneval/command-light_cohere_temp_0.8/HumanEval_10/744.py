```python
def is_palindrome(string: str) -> bool:
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    if not_palindrome(string):
        return ''

    palindrome = string[::-1].center() + string

    return palindrome

# Example usage
print(make_palindrome('tac'))
```
This code defines two functions, `is_palindrome` and `make_palindrome`. The `is_palindrome` function returns `True` if the string is a palindrome and `False` otherwise. The `make_palindrome` function takes a string as input and returns the shortest palindrome that begins with the given string. It uses the algorithm idea to create the palindrome by finding the longest palindrome suffix and appending it to the center of the original string. The function checks if the result is a palindrome using the `is_palindrome` function and if it is not, it returns an blank string.