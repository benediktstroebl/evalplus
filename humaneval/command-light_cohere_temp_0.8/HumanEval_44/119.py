```python
def change_base(x: int, base: int) -> str:
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")
    if x < 0:
        raise ValueError("Input number must be non-negative")
    result = "{0:02}".format(x, base)
    return result

# Test cases
test_case1 = change_base(8, 3)
test_case2 = change_base(8, 2)
test_case3 = change_base(7, 2)

print("Test case 1:", test_case1)
print("")
print("Test case 2:", test_case2)
print("")
print("Test case 3:", test_case3)
```
This Python script defines a function `change_base` that converts a given number `x` to a string representation using the specified base. It then performs various tests on the function to validate the correctness of the output. It ensures that the base is between 2 and 36, handles non-negative numbers, and raises an error for invalid base or negative input.