```python
def change_base(x: int, base: int) -> str:
    """
    Changes the base of a number to another base.
    Args:
        x: int, the number to be converted
        base: int, the base to which the number is converted
    Returns:
        str: the converted number as a string
    """
    if x < 0:
        x = abs(x)

    res = ""
    while x > 0:
        temp = x % base
        x //= base
        res += str(temp)
    return res

# Test case 1
print(change_base(8, 3))  # Expected Output: '22'

# Test case 2
print(change_base(8, 2))  # Expected Output: '1000'

# Test case 3
print(change_base(7, 2))  # Expected Output: '111'
```
This code defines the `change_base` function, which takes an integer `x` and a base `base` as input and returns the converted number as a string. The function first handles negative numbers, ensuring they are converted to positive values, then proceeds with the loop that converts the number using the specified base. It utilizes the string formatting to display the result as a readable number.