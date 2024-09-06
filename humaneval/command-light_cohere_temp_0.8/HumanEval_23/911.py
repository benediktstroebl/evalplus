```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Tests
string1 = "" # empty string
assertEqual(strlen(string1), 0)

string2 = "abc" # simple string
assertEqual(strlen(string2), 3)

string3 = "" # empty string again
assertEqual(strlen(string3), 0)

string4 = "abc" # longer string
assertEqual(strlen(string4), 6)
```