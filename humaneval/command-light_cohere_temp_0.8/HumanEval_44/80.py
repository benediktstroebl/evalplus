```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of input number x to base base.
    :return string representation after conversion.
    base numbers less 10
    if not (base < 2 or base > 36):\
            raise ValueError("Base number is invalid")
    return f'{x} ({base})'

test_change_base = []
test_change_base.append([str(change_base(12, 10), test_change_base))])
test_change_base.append([str(change_base(12, 37), test_change_base))])
test_change_base.append([str(change_base(12, 1), test_change_base))])
test_change_base.append([str(change_base(-12, 10), test_change_base))])
test_change_base.append([str(change_base(-12, 37), test_change_base))])
test_change_base.append([str(change_base(-12, 1), test_change_base))])
```