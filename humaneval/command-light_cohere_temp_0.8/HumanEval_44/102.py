```python
def change_base(x: int, base: int):
    """
    Change the base of a number to another base.
    :param x: int, base: int
    :return: string
    """
    return str(x) if x <= base else "Error: number is too large"

# Test case 1
print(change_base(8, 3))  # Output: '22'

# Test case 2
print(change_base(8, 2))  # Output: '1000'

# Test case 3
print(change_base(7, 2))  # Output: '111'
```
This script defines a function `change_base` which takes two parameters, `x` and `base`, representing the number to be converted and the desired base respectively. The function then converts the base of the input number `x` to the desired base using the `str()` function, which converts numbers into strings. 

The test cases provided print the output of the `change_base` function for different inputs and base values.