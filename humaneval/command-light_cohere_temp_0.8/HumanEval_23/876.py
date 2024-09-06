Here's a self-contained Python function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """Return length of given string"""
    return len(string)

# Test cases
test_strlen = {
    "":        pass

# empty string
    "".join_str
    assert strlen("") == 0

# simple string
    "abc"
    assert strlen("abc") == 3

# multi-character strings
"abc123"
    assert strlen("abc123") == 7

# non-ascii strings
"﻿abc"
    assert strlen("﻿abc") == 5

# empty string and non-string values
5abc
5
None
}
```