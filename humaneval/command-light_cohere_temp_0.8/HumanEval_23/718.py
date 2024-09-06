Here is a self-contained Python script with a function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Returns length of the given string"""
    return len(string)

# Test cases
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
print(strlen('abcde'))  # Output: 5
print(strlen(''))    # Calls default argument case, returns 0
print(strlen('A'))  # Output: 1
```

This code defines a function `strlen` that calculates the length of a given string. It passes all test cases successfully and provides an elegant, self-contained solution to the problem statement.