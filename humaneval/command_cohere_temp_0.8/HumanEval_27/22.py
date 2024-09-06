```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script provides a function that accepts a string as an argument and returns a new string where the case of letters has been flipped. It employs a list comprehension that checks if each character of the string is alphabetical with the `isalpha()` string method. If a character is alphabetic, it is flipped using the `swapcase()` method. Non-alphabetic characters like punctuation, digits, etc. are left unchanged and passed through the filter. The final string is constructed by concatenating the resulting list.

The example usage in the docstring demonstrates this by returning 'hELLO' for the input 'Hello'. You can confirm this by importing the function and calling it with your input:
```python
import string

def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)

# Example usage:
input_string = 'Hello, World!'
result = flip_case(input_string)
print(result)
```

This will print 'hELLO, wORLD!' with the letters flipped and the non-alphabetic characters remain unchanged.