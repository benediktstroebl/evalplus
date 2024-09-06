```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base
    provided.
    :return: string representation of the converted number
    """
    if x < 0 or base < 2:
        raise ValueError("Invalid base or number")
    if base == 2:
        return f'{x}'
    result = str(x, base)
    return result

# Unit tests
def test_change_base():
    base_cases = [2, 10, 111, -33]
    assert change_base(7, base_cases[0]) == '7777'
    assert change_base(123, base_cases[1]) == '1001100'
    assert change_base(-12, base_cases[2]) == '-120'
    assert change_base(42, base_cases[3]) == '20000000'
test_change_base()
```
This code defines a function `change_base` that converts a given number to a specified base. It also provides several tests cases to check the function's correctness.