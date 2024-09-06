Here's the code that solves the given markdown code length calculation function:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test cases
string1 = ""
assert strlen(string1) == 0

string2 = "abc"
assert strlen(string2) == 3

string3 = "spaces"
assert strlen(string3) == 0

string4 = "abc\nabc"
assert strlen(string4) == 3
```

I hope that this code includes self-contained tests to verify the correctness of the `strlen` function.  I hope this read it explanation for further details.