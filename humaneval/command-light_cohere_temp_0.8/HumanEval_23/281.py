Here is a self-contained Python script that defines a function `strlen` which calculates and returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test cases
print(strlen(''))      # Output: 0
print(strlen('abc'))   # Output: 3
print(strlen('hello world')) # Output: 13
```
This script's function `strlen` takes a string as input and returns its length using the `len()` function.  The example test cases show how the function behaves for different inputs.