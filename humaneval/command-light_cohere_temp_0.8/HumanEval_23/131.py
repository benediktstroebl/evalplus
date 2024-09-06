```python
def strlen(string: str) -> int:
    return len(string)

# Test the function with various inputs
string1 = ""
string2 = 'abc'
print(strlen(string1))  # Output: 0
print(strlen(string2))  # Output: 3

string3 = '123'
string4 = 'abc123'
print(strlen(string3))  # Output: 5
print(strlen(string4))  # Output: 6

# Using str.join() for a concatenation
string5 = 'hello ' + 'world!'
print(strlen(string5))  # Output: 10
```