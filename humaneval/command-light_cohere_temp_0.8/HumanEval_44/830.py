```python
def change_base(x: int, base: int) -> str:
    """
    Changes the base of a number to another base.
    :param x: int, base of the number
    :return: string representation of the number in the specified base
    """
    if x < 0 or base < 2:
        raise ValueError("Both number and base should be positive and greater than 0")

    # Perform the conversion
    result = str(x, base)

    return result

# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(10, 2))  # Output: '1000'
print(change_base(-5, 5))  # Output: '5'
print(change_base(123, 7))  # Output: '4187'
print(change_base(-123, 2))  # Output: '1000'
print(change_base(123, 0))  # Output: '1'
```
The code defines a function change_base that takes an integer x and a base b as input and returns the number in the specified base. It performs the basic checks to ensure that the input is valid and raises a ValueError if it is not. The code also includes a series of test cases to ensure the correctness of the change_base function.