```python
def change_base(x: int, base: int):
    """
    Change the base numerical representation of input number x to base base.
    return string representation after conversion.
    base numbers are recommended to be 10, 2, or 16.
    """
    numbers may be converted using the following format: ####'#x####' ####'
    """
    return str(x).format(x, f'{base}'))

x = 8
y = 3
test_change_base = {
    "test 1": lambda: change_base(x, y) == '22'
    "test 2": lambda: change_base(x, 2) == '100'
    "test 3": lambda: change_base(x, 16) == '100000000'
    "test 4": lambda: change_base(y, 10) == '30'
    "test 5": lambda: change_base(7, 2) == '111'
}

for test in test_change_base:
    print(test)
```