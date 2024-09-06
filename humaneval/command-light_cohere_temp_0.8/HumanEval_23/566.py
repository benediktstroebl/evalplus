Here is a Python script that calculates the length of the given string:

```python
def strlen(string: str) -> int:
    """ Returns length of the given string"""
    return len(string)

# Test case 1
print(strlen(''))
# Prints: 0

# Test case 2
print(strlen('abc'))
# Prints: 3
```

The `strlen()` function calculates the length of the given string using the `len()` function. The output for test case 1 is 0, and the output for test case 2 is 3. The test cases pass the test successfully.