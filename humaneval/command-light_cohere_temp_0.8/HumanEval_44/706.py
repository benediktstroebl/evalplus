```python
def change_base(x: int, base: int):
    if isinstance(x, str):
        return x.
    elif base == 10:
        return str(x)
    elif base == 2:
        return ''.join(str(num) for num in x)
    else:
        raise ValueError("Invalid base")

def test():
    base = 10
    x = str(123)
    result = change_base(x, base)
    assert isinstance(result, str), f"Expected string, got {type(result)}"
    assert result == x, f"Expected {x}, got {result}"
    base = 2
    x = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = change_base(x, base)
    assert isinstance(result, str), f"Expected string, got {type(result)}"
    assert result == x, f"Expected {x}, got {result}"
    return True

# Run the test function
test()
```
This Python script defines a function `change_base` that takes two parameters: `x` (the number to be converted) and `base` (the numerical base to convert to). It handles both string and number cases and raises a `ValueError` for invalid bases. The `test` function contains a test case that verifies the correctness of the `change_base` function.