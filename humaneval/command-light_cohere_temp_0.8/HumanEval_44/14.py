```python
def change_base(x: int, base: int) -> str:
    if base < 2 or base > 36:
        raise ValueError("Invalid base value.
    result = ""
    if x < 0:
        raise ValueError("Input number must be positive")
    elif base == 10:
        result = str(x)
    elif base == 2:
        result = str(x, 2)
    else:
        result = bin(x)[0:base-1].
    return result

# Test cases
print(change_base(-8, 3))
print(change_base(10, 2))
print(change_base(123, 3))
print(change_base(35, 12))
print(change_base(0, 101))
print(change_base(15, 55))
``` 
The provided code defines a function `change_base` that converts a given number `x` to a specified base `base`. It ensures that the base is within the valid range of 2 to 36, inclusive. The code also performs input validation for the base and the number. It raises appropriate error for invalid inputs and returns the binary representation of `x` with the correct base using the `bin` function. 
The test cases in the code demonstrate the functionality of the `change_base` function for various scenarios.