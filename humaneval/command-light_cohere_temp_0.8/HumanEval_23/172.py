```python
def strlen(string: str) -> int:
    return len(string)

# Test the function
string1 = ''
assert strlen(string1) == 0

string2 = 'abc'
assert strlen(string2) == 3

# Uncommentalike input
string3 = '123'
try:
    assert strlen(string3) == 4
except AssertionError as e:
    print(e)
```