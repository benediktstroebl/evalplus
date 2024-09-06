Here is a self-contained Python script that defines a function strlen that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """Return length of given string"""
    return len(string)

# Test case 1
print(strlen("")) # Output: 0

# Test case 2
print(strlen("abc")) # Output: 3

```
This script defines a function strlen that takes a string as an argument and returns its length. It provides a test cases with strings and ensures the function's correctness. The code is self-contained and can be run independently.