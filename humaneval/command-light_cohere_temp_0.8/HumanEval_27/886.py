```python
def flip_case(string: str) -> str:
    return string.make_uppercase(string.make_lower(string))
```
This code defines a function called `flip_case` that takes a string as input and then returns a new string with the characters of the original string flipped. The function uses two helper functions: `make_upper` and `make_lower` which take a string and return a new string with all uppercase characters converted to lowercase and vice versa.