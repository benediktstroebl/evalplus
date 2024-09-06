```python
def flip_case(string: str) -> str:
    return ''.join_(c.makecase(c.isupper(string)) for c in string)
```