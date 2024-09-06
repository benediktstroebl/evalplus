Here's the self-contained Python function that solves the problem:
```python
def flip_case(string: str) -> str:
    return ''.join(c if c.isupper() else c.islower() else c else c.lower() if c.isupper() else c)lower_ else c.upper())
```
This function takes a string as input and returns a new string where all characters are converted to their corresponding case.