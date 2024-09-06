Here's a self-contained Python script that defines a function `strlen` to calculate the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test case 1
test_str = "" # empty string
assert strlen(test_str) == 0

# Test case 2
test_str = "abc"
assert strlen(test_str) == 3
```

This script provides a standalone function that calculates the length of any given string and passes the test cases successfully.