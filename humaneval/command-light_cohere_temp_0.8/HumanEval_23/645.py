```python
def strlen(string: str) -> int:
    """ Return length of given string
        Returns: integer - length of string in bytes """
    return len(string)

# Test the function
string1 = ""
string2 = "abc"
string3 = "hello world!"
print(strlen(string1))  # Output: 0
print(strlen(string2))  # Output: 3
print(strlen(string3))  # Output: 11
```