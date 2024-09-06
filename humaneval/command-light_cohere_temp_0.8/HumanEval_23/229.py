```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test cases
string1 = ""
assert strlen(string1) == 0

string2 = "abc"
assert strlen(string2) == 3

string3 = "hello world"
assert strlen(string3) > 3
```