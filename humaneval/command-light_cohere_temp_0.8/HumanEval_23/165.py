```python
def strlen(string: str) -> int:
    return len(string)

# Testing the function
string1 = ''
assert strlen(string1) == 0

string2 = 'abc'
assert strlen(string2) == 3

string3 = 'hello world'
assert strlen(string3) > 5
```