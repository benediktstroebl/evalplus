```python
def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base B"""
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")
    if x < 0 or not isinstance(x, int):
        raise ValueError("Input must be a number")

    # Use string formatting to convert to desired base
    return format(x, f"{base}")

# Test the function with various cases
test_change_base = []
test_change_base.append([1, 8, 3])
test_change_base.append([2, 8, 2])
test_change_base.append([3, 7, 2])
test_change_base.append(4, "1", 2])
test_change_base.append(5, "1000", 2)
test_change_base.append(6, "111", 2)
test_change_base.append(7, "1", 2)

# Run the function on the test cases
for case in test_change_base:
    assert change_base(case[0], case[1]) == case[2]
```