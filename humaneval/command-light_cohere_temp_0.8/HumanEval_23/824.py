```python
def strlen(string: str) -> int:
    """ Returns length of the given string"""
    return len(string)

# Test the function
string1 = "" # empty string
print(strlen(string1))  # Output: 0

string2 = "abc" # string with characters
print(strlen(string2))  # Output: 3

string3 = " Hello World!" # this will have 2 spaces at the end
print(strlen(string3))  # Output: 4
```