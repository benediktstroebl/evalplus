```python
def flip_case(string: str) -> str:
    return ''.join() if not string else string.tolower() if not string[0] else string[0].toUpperCase() + string[1:]

# Test case:
print(flip_case('hello')) # Output: 'HELO'
```
The function `flip_case` takes a string as input and returns a new string where the first character is converted to uppercase if the original string is not empty.