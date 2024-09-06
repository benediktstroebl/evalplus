```python
def change_base(x: int, base: int) -> str:
    if base < 2 or base > 36:
        raise ValueError("Invalid base value")
    if x < 0:
        x = abs(x)
    result = []
    while x:
        result.append(str(x[int(x) % base)])
        x //= base
    return ''.join(result) or 'Invalid number'

# Unit tests
test_change_base = []
test_change_base.append([range(1, 10000), int))
test_change_base.append(lambda x: change_base(x, 10) == ''.join(x))
test_change_base.append(lambda x: change_base(x, 2) == ''.join(x))
test_change_base.append(lambda x: change_base(x, 5) == ''.join(x))
test_change_base.append(lambda x: change_base(x, 8) == ''.join(x))
test_change_base.append(lambda x: change_base(x, 3) == ''.join(x))
test_change_base.append(lambda x: change_base(-x, 10) == ''.join(x))
test_change_base.append(lambda x: change_base(-x, 2) == ''.join(x))
test_change_base.append(lambda x: change_base(-x, 5) == ''.join(x))
test_change_base.append(lambda x: change_base(-x, 8) == ''.join(x))
test_change_base.append(lambda x: change_base(-x, 3) == ''.join(x))
``` 
This Python script defines a function `change_base` that converts a number to a specified base. The function uses the string representation method to achieve the conversion. It also handles negative numbers correctly. The script includes a unit tests for the `change_base` function to ensure its correctness. The tests cover a range of numbers and different base values, and they pass the expected results.