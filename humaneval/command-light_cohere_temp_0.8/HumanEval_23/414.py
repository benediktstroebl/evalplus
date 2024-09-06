```python
def strlen(string: str) -> int:
    return len(string)

# Testing the function
string1 = ""
assertEqual(strlen(string1), 0)

string2 = "abc"
assertEqual(strlen(string2), 3)

# Using the function
string3 = "hello world"
print("Length:", strlen(string3))
```