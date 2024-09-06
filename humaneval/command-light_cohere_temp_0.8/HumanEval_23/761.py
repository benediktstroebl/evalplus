Here's a self-contained Python script with a function that calculates and returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test the function with different input strings
# ensure the function returns the expected results
str1 = ""
print(strlen(str1))  # Output: 0
str2 = "abc"
print(strlen(str2))  # Output: 3
str3 = "hello world"
print(strlen(str3))  # Output: 11
```