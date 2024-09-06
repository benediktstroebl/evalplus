```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script provides a function that takes a string as an argument and flips the case of alphabetic characters only, leaving non-alphabetic characters unchanged. For example:
```python
print(flip_case('Hello World'))  # Outputs: 'hELLO WORLD'
```

This approach uses a list comprehension to iterate through each character in the input string. For alphabetic characters, the `swapcase()` method is used to interchange their case. Non-alphabetic characters (e.g., punctuation) are left as is.