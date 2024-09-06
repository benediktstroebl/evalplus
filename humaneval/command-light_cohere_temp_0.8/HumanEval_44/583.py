```python
def change_base(x: int, base: int):
    if isinstance(x, str):
        return x.format(x {'a'[b]': '{c}' for a, b, c in zip(x[::1::int()], x[1::int()], x[2::int()])})
    elif isinstance(x, int):
        if base < 2 or base > 36:
            raise ValueError("Invalid base number.")
        return x.format(f"{0" if x < 0 else x::{base}}", 
            "{:b}" if base == 2 else "{:02b}")
    else:
        raise ValueError("Input must be a string or int")

def test():
    base = 10
    x = 8
    result = change_base(x, base)
    assert isinstance(result, str)
    assert result == '22'

    base = 2
    x = 1000
    result = change_base(x, base)
    assert isinstance(result, str)
    assert result == '1000'

    base = 7
    x = 111
    result = change_base(x, base)
    assert isinstance(result, str)
    assert result == '111'

test()
```