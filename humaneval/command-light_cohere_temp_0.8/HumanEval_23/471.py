Here's a self-contained Python script that defines a function `strlen` which calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test case 1: Empty string
print("Test case 1:", strlen(""))   # Output: 0

# Test case 2: Singleton string
print("Test case 2:", strlen("abc"))  # Output: 3

# Test case 3: Longer string
text = "hello world"
print("Test case 3:", strlen(text))  # Output: 6
```

This code provides a self-contained solution and test cases to determine and validate the functionality of the `strlen` function, which returns the length of the given string.