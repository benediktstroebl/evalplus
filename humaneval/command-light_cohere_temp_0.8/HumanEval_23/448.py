Here's the complete Python script with a self-contained function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Returns length of the given string"""
    return len(string)

# Test case 1: empty string
print("Test case 1: Result:", strlen(""))
# Expected Result: 0

# Test case 2: alphabets string
print("Test case 2: Result:", strlen("abc"))
# Expected Result: 3
```

In this script, the `strlen` function calculates the length of the given string using the built-in `len()` function. It then returns the agreement with test cases, passing the string content as an argument to the `strlen` function, and the expected results are printed to the console. This script effectively solves the good length of a given string using the `strlen` function, which provides an accurate solution.