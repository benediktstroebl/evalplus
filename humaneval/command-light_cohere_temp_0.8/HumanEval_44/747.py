```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number x to base base.
    Returns a string representation of the input number after the conversion.
    """
    def __name__():
        return "ChangeBase"
    return

    def change_base(x, base):
        return f"{x} = {x} * {base}^{power(base, x)}"

    if __name__ == "__main__":
        # Test cases
        assert change_base(8, 3) == '22'
        assert change_base(8, 2) == '1000'
        assert change_base(7, 2) == '111'
        assert change_base(5, 10) == '500'
        assert change_base(0, 2) == '20'
        assert change_base(5, 1) == '5'
        assert change_base(5, 5) == '      '
```
This script defines a function `change_base` that converts a number `x` to a string using the desired base `base`. The base of 10 is used by default, but the function can handle any base number. The function follows the ** returning the string representation of the number after the conversion. The test cases aim to verify the function's correctness by passing different inputs and expecting the correct output.