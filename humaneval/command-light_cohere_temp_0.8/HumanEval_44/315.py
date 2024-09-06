```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of the input number x to base base.
    return the string representation after conversion
    base numbers less than 36 are converted to string using 'format'.
    """
    if base < 36:
        return format(x, f"{base}")
    else:
        raise ValueError("Base number is out of range")
    return "base out of range"

# Unit tests
test_change_base = []
test_change_base.push((8 test("8", 3))
test_change_base.push((8 = 8, 2))
test_change_base.push((7, 2))

for case, test in test_change_base:
    print(f"{case} : {change_base(int(case), int(base))}")
```