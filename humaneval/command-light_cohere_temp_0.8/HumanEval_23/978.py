Here's a self-contained Python function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test case 1: empty string
print(strlen(""))
# Output: 0

# Test case 2: abc as a string
print(strlen("abc"))
# Output: 3
```

Please note, the code defines a function `strlen` that takes a string as an argument and returns its length. This function is optimized for efficiency, as it utilizes the built-in `len()` function to directly get the length of the input string.