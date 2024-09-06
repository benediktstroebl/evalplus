```python
def flip_case(string: str) -> str:
    return ''.join(c if c.isupper() else(c.islower()) else(c.isupper()) else(c) else c) for c in string)
```