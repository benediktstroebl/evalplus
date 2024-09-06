Here is a self-contained Python script that solves the problem of calculating the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test case 1
print(strlen(''))

# Test case 2
print(strlen('abc'))
```

This script defines a function `strlen` that takes a string as an argument and returns its length. The function uses the `len` function to calculate the length of the input string.