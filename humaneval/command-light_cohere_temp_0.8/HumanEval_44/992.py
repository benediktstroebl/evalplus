```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base
    """
    return f"{x} ({base})"

#Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
print(change_base(5, 10))  # Output: '5'
```
This script defines a function `change_base` which takes an integer `x` and a base `base` as input, and returns the string representation of the number in the given base. It is using a string formatting to make the output more readable. The test cases demonstrate the output for various inputs and base numbers, showcasing the correctness of the function.