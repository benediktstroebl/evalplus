```python
def change_base(x: int, base: int):
    """
    Convert a number to a string representation using the specified base.

    Args:
        x: int, the number to be converted
        base: int, the base to use for conversion
    Returns:
        string, the string representation of x using the specified base
    """
    # handle negative numbers by converting to positive and putting base as string before negative
    if x < 0:
        x = abs(x)
        base = str(base) + " " + '-'
    return format(x, '{base}')

#unit tests
test_change_base = [
    ("8", 3, "22"),
    ("8", 2, "1000"),
    ("7", 2, "111"),
    (-5, 10, "-50"),
    (-10, 10, "-100"),
    # complex test case
    (10 ** 5), 2, "?$#@!"
]

if __name__ == "__main__":
    for x, b, y in test_change_base:
        assert change_base(x, b) == y, f"Failed: {x}:{b} != {y}"
```
This script defines a function `change_base` that converts a number to a string using a specified base. It also provides a read tests for the function using the `unittest` library, passing the `test_change_base` list of test cases. 

The tests include a variety of scenarios, including positive and negative numbers, various bases, and complex numbers. The function's output is compared to the expected result, and the test passes if the comparison is successful.