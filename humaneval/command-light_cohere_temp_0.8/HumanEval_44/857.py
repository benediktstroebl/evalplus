```python
def change_base(x: int, base: int) -> str:
    if not isinstance(x, int) or not isinstance(base, int):
        raise TypeError("Input must be an integer")

    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")

    if base == 10:
        return str(x)

    result = []
    while x > 0:
        result.append(str(x % (x, base)))
        x -= x & -x

    return ''.join(''.join(result)

# Unit tests
test_change_base = []
test_change_base.append(
    [10, '101010'),
    (5, '05'),
    (20, '20'),
 (123, '123'),
 (0, ''),
 (360,-1),
)

test_change_base.append(
    ("8", 8, ''),
    ("123", 123, ''),
)

print('Results of the test cases:')
for test in test_change_base:
    assert change_base(*test) == test[1], f"Failed: {test[0]} != {test[1]}"
``` 
This Python code defines a function `change_base` that converts a number to a specified base. It uses this `assert` statement with the `test_change_base` list of test cases to check if the function is working correctly. The output is the test results and provides feedback on whether the test cases are successful.