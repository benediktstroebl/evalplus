Here's the self-contained Python script that solves the task of calculating the length of a given string:
```python
def strlen(string: str) -> int:
    """ Returns length of the given string."""
    return len(string)

# Test case 1: empty string
print(strlen(''))
# Expected Output: 0

# Test case 2: with ASCII characters only
print(strlen('abc'))
# Expected Output: 3
```

This script defines a function `strlen` that calculates the length of a given string. It passes the basic test cases, where empty strings and strings with only ASCII characters are passed to the function, and the output is correctly printed.