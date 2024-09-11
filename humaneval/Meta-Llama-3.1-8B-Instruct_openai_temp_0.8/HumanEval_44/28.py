```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    :param x: input number
    :param base: target base
    :return: string representation of the input number in the target base
    """
    if x < base:
        return str(x)
    else:
        return change_base(x // base, base) + str(x % base)

# Test cases
def test_change_base():
    assert change_base(8, 3) == '22'
    assert change_base(8, 2) == '1000'
    assert change_base(7, 2) == '111'

test_change_base()
print("All test cases pass")
```

In this script, we define a recursive function `change_base(x, base)` that takes an integer `x` and a target base `base` as input. The base case is when `x` is less than the target base, in which case we simply convert it to a string. Otherwise, we recursively convert the integer part of `x` divided by the base and append the remainder to the result. The test cases at the end verify the correctness of the function.