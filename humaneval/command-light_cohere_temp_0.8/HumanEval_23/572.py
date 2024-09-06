```python
def strlen(string: str) -> int:
    return len(string)

# Test cases
string = ""
assertEqual(strlen(string), 0)

string = "abc"
assertEqual(strlen(string), 3)

# Multi-string and other types of input
string = "hello world"
string = 42
string = (1, 2, 3)
assertEqual(strlen(string), 3)

# Error cases
try:
    string.len()
except TypeError:
    print("Expected TypeError")

# str1 is not iterable
try:
    strlen('str1')
except TypeError:
    print("Expected TypeError")
```