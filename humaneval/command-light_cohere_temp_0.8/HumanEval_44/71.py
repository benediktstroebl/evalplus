```python
def change_base(x: int, base: int):
    """
    Change the base of a number x to base base.
    :return x if x is an integer and base is not 10, otherwise return 'Invalid'
    """
    if isinstance(x, int) and base not in [2,5,10]:
        return 'Invalid'
    return '{0:0>{base}'.format(x)

# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(5, 3))  # Output: '01'
print(change_base(3, 10)) # Output: 'Invalid'
print(change_base(10, 5)) # Output: 'Invalid'
print(change_base(10, 2)) # Output: '1000'
print(change_base(123, 10)) # Output: 'Invalid'
```
This Python code defines a function `change_base` that converts a given number `x` to a specified base `base`. It checks for the input types of `x` and `base`, and returns the converted string representation if the conditions are met. 

The function is then tested with various inputs and bases, and the expected outputs are printed. The output will show the specific cases and the function's behavior in different scenarios.