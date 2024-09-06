Certainly! Here's a self-contained Python script that defines a function `strlen` solving the length of a given string:

```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test case 1
test_str = ""
assert strlen(test_str) == 0

# Test case 2
test_str = "abc"
assert strlen(test_str) == 3
```

This script defines a function `strlen` that takes a string as an argument and returns its length. The function uses the basic Python `len()` function to calculate the length of the given string.