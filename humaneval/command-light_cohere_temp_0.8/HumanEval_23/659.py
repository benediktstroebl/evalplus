Here is a self-contained Python script that defines a function `strlen` which calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test cases
string1 = "" # Empty string
assert strlen(string1) == 0

string2 = "abc" # Simple string
assert strlen(string2) == 3

string3 = "abcdef" # Longer string
assert strlen(string3) == 6

# Both empty string and single character string pass tests
string4 = ""
assert strlen(string4) == 0

string5 = "a" # Single character string
assert strlen(string5) == 1
```