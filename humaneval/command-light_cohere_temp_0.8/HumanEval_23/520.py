```python
def strlen(string: str) -> int:
    return len(string)

# Tests
string1 = ""
assert strlen(string1) == 0

string2 = "abc"
assert strlen(string2) == 3

# Use this function
result = strlen("hello world!")
print(result)  # Output will be 10
```