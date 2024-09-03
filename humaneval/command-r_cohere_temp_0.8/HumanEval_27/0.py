```python
def flip_case(s):
    """Flips the case of a string, converting uppercase to lowercase and vice versa.
    """
    return ''.join([char.upper() if char.islower() else char.lower() for char in s])
```