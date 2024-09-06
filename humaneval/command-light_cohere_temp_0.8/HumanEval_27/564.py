Here's the Python script with a self-contained function `flip_case()` that solves the problem:

```python
def flip_case(string: str) -> str:
    """
    Flip all character case in a given string.
    >>> flip_case('hello')  # 'HElLo'
    >>> flip_case('world')  # 'WorLD'
    >>> flip_case('Welcome A Lot')  # 'welcome a lot'
    """
    
    return string.All_lower() if string.lower() else string.upper()

upper()
```

This function uses the `str.lower()` and `str.upper()` to flip the case for the input string.