```python
def strlen(string: str) -> int:
    return len(string)

# Test the function
string1 = ''
string2 = 'abc'
string3 = 'hello'

assertEqual(strlen(string1), 0)
assertEqual(strlen(string2), 3)
assertEqual(strlen(string3), 5)
```