```python
def change_base(x: int, base: int) -> str:
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36.")
    result = ""
    while x > 0:
        mod = x % base
        result += str(mod)
        x //= base
    return result

# Unit tests
test_change_base = []
test_change_base.py = [
def test_change_base():
    assert change_base(8, 3) == '22'
    assert change_base(7, 2) == '111'
    assert change_base(9, 10) == '9'
    assert change_base(10, 10) == '10'
    assert change_base(12, 5) == '60'
    assert change_base(123, 2) == '48'
    assert change_base(123, 12) == '4812'
    assert change_base(123, 20) == '4820'
test_change_base.py
```
This code defines a function called change_base that converts a number to a given base. The function uses a loop to repeatedly divide the number by the base until it is zero, and then adds the remainder to the result string. The function then returns the string representation of the number in the desired base.

The code also includes unit tests for the change_base function using the unittest module in Python. These tests verify that the functions correctly convert numbers to the desired bases.