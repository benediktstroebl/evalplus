Here is a self-contained Python function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test case 1
string1 = ""
assertEqual(strlen(string1), 0)

# Test case 2
string1 = "abc"
assertEqual(strlen(string1), 3)
```
This code defines a function `strlen` that calculates the length of a given string. It uses the straightforward Python's `len()` function to get the length.

This code is self-contained and will provide the solution to the problem you have provided.