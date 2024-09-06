```python
def change_base(x: int, base: int):
    if base == 10:
        return str(x)
    elif base in [2, 36]:
        return str(x).format(x, '#{base}'))
    else:
        raise ValueError("Invalid base number")

# Test cases
test_cases = [
    (8, 3),
    (8, 2),
    (7, 2),
    (10, 10),
    (10, 36),
    (15, 10),
    (16, 36),
]

for x, base in test_cases:
    result = change_base(x, base)
    assert result == str(x), f"Failed for {x} and base {base}."
``` 
This script defines a function `change_base` that converts a given number to a specified base. The function handles the `base` and `x` arguments and returns the resulting string representation. The test cases ensure that the function works correctly for different inputs and base numbers.