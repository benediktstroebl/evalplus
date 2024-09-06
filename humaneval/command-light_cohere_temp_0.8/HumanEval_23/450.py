```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test the function with various inputs
str1 = ""
assert strlen(str1) == 0

str2 = "abc"
assert strlen(str2) == 3

# Long string
str3 = "Hello, World! This is a long text"
assert strlen(str3) == 29 

# Invalid input
str4 = 42 
assert strlen(str4) == 0 

print("All tests passed!")
```