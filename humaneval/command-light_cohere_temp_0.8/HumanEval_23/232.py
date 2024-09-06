Here is a self-contained Python script that defines a function strlen that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    return len(string)

# Test case 1
assert strlen('') == 0

# Test case 2
assert strlen('abc') == 3
```

This script defines a function `strlen` that calculates the length of a given string, and passes the tests shown. The test cases ensure that the function correctly calculates the length of the provided string.