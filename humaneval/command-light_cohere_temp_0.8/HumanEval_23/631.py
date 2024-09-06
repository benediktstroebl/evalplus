Here is a self-contained Python script that defines a function strlen, which calculates and returns the length of a given string:
```python
def strlen(string: str) -> int:
    """Return length of given string"""
    return len(string)

# Testing the function
# Ensure empty string gets length 0
assert strlen('') == 0

# Test case 1:
string = 'abc'
assert strlen(string) == 3

# Test case 2:
string = 'hello world'
assert strlen(string) > 3
```