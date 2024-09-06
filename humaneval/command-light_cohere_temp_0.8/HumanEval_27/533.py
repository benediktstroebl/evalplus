```python
def flip_case(string: str) -> str:
    return ''.joinimalize(string.make_lower(string))
```
This function uses a helper function called `make_lower` that converts a given string to lowercase, and another helper function called `normalize` that uses `str.make_lower` to flip the characters between lowercase and uppercase.