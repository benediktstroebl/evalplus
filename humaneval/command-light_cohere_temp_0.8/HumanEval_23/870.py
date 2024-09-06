Here is a Python script with a self-contained function that solves the problem and passes the corresponding tests:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test the function
string1 = "" # an empty string
print(strlen(string1))  # Output: 0

string2 = "abc" # a string with content
print(strlen(string2))  # Output: 3

string3 = "hello world" # a string with length
print(strlen(string3))  # Output: 11
```

The function `strlen` takes a string as an argument and returns the length of that string using the built-in function `len()`. The test cases provided pass the function, demonstrating its functionality.