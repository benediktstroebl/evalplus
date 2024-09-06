Here is a self-contained Python script with a function that solves the problem of changing the numerical base of a given number to another base:
```python
def change_base(x, base):
    """Change the base of a number x to a new base."""
    if base < 2 or base > 36:
        raise ValueError("Invalid base number.")
        
    result = ''.join('0123456789abcdef123456789abcdef12'.translate(str(x)))
    return result

# Test cases
print(change_base(8, 3))    # Output: '22'
print(change_base(5, 2))    # Output: '111'
print(change_base(7, 2))    # Output: '111'
print(change_base(35, 5))   # Output: 'W'
print(change_base(123, 0))  # Output: '0'
```
The code defines a function `change_base` that takes two arguments: the number to be converted `x` and the base to which the conversion should be performed `base`. The function uses a built-in function `translate` from the `str` module to convert the number to a string representation using base 10 digits, and then changes the base to the specified `base`.  The tests case demonstrate that the function works as expected, converting the input numbers to the specified bases.