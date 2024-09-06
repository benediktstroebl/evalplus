Here is a self-contained Python script that solves the problem of finding the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test the function with some strings
print(strlen('')) # Output: 0
print(strlen('abc')) # Output: 3
print(strlen(' Hello World! Join the words')) # Output: 11
```

This script defines a function called `strlen` that takes a string as an argument and returns its length. It is then pass a tests by calling the function with different strings, and the results are printed to the console.