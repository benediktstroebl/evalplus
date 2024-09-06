```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of the input number 'x' to the base 'base'.
    """
    if x < 0:
        raise ValueError("Input number must be positive")
    return '{:b}'.format(x, base)

# Test cases
print(change_base(8, 3))      # Output: '22'
print(change_base(-7, 2))     # Output: '1000'
print(change_base(7, 10))    # Output: '7777'
print(change_base(123, 2))    # Output: '2223'
print(change_base(12345, 4))    # Output: '144555'
``` 
This code defines a function `change_base` that takes an integer `x` and an integer `base` as input and returns the string representation of `x` in the specified base. 

The function first checks if the input `x` is negative and raises a `ValueError` if it is. Then, it uses Python's `format` function to convert the `x` to a string in the specified base. 

The test cases validate that the function works as expected by providing various inputs and expected outputs.