```python
def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base.
    base numbers use 10
    to decimal base.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(56, 1)
    TraceError: invalid literal for enum 'int': '56'
    """
    if base not in [2, 5, 10]:
        raise ValueError("Base number must be 2, 5, or 10.")
    
    if base == 10:
        return str(x)
    
    if base == 2:
        return f"{x:02}".zfill()
    
    return f"{x:05}".zfill()

def test_change_base():
    x = 56
    base = 1
    result = change_base(x, base)
    assert result == "56"
```
This script defines a function `change_base` that converts numbers to a desired base. The `test_change_base` function tests this function with a specific input and base to ensure the correctness of the `change_base` function.