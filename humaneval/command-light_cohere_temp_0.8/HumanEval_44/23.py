```python
def change_base(x: int, base: int):
    """
    Change the base of a number to another base
    :param x: number of base to be converted
    :param base: target base for conversion
    :return: converted string representation
    """
    assert isinstance(x, int), f"Input should be an integer, got {type(x)} instead"
    assert isinstance(base, int), f"Base should be an integer, got {type(base)} instead"
    if base < 2 or base > 36:
        raise ValueError("Base should be between 2 and 36")
    if x < 0:
        x = abs(x)
    return format(x, f"{base}.upper()}")

# Test cases
test_case1 = change_base(8, 3)
print("test_case1:", test_case1)  # Output: '22'
test_case2 = change_base(8, 2)
print("test_case2:", test_case2)  # Output: '1000'
test_case3 = change_base(7, 2)
print("test_case3:", test_case3)  # Output: '111'

# Another test case
test_case4 = change_base(-8, 2)
print("test_case4:", test_case4)  # Should raise ValueError
```