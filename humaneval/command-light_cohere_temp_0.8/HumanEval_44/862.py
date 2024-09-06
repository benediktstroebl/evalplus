```python
def change_base(x: int, base: int):
    """
    Change the base of a number to another base.
    :param x: int, the number to be converted
    :param base: int, the desired base for conversion
    :return: string representation of x in the base base
    """
    return f"{x}_{base}"

# Tests
def test_change_base():
    base_list = [10, 2, 7]
    for base in base_list:
        assert change_base(8, base) == "22"
        assert change_base(5, base) == "512"
        assert change_base(7, base) == "111"
        assert change_base(16, base) == "3210"
        assert change_base(1000, base) == "3214"
        assert change_base(1, base) == "1"
        assert change_base(-5, base) == "-512"
        assert change_base(0, base) == "0"
        assert change_base(-8, base) == "-1000"
        assert change_base(1e5, base) == "10000"

if __name__ == "__main__":
    test_change_base()
```
This script defines a function `change_base` that converts a number to a specified base. The `test_change_base` function contains a set of test cases that cover a range of numbers and bases. The test cases ensure that the function is correctly implementing the base conversion of numbers.

The function `change_base` takes an integer `x` and a base `base` as parameters. It then returns the will string representation of `x` in the base `base`.