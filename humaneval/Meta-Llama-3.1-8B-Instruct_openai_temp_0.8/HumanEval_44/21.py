### Convert Number to Different Base
#### Code
```python
def change_base(x: int, base: int) -> str:
    """
    Change numerical base of input number x to base.
    
    Args:
    x (int): The number to be converted.
    base (int): The base to convert to (less than 10).
    
    Returns:
    str: The string representation of x in the specified base.
    
    Examples:
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if x == 0:
        return '0'
    
    digits = '0123456789'
    base_digits = digits[:base]
    
    if x < base:
        return base_digits[x]
    
    result = ''
    while x > 0:
        result = base_digits[x % base] + result
        x //= base
    
    return result

# Test the function
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

#### Explanation
This function converts an integer `x` to a specified base (less than 10).
To do this, it uses the following steps:

1.  If `x` is 0, it immediately returns '0'.
2.  It constructs a string `digits` containing all possible digits (0-9) and another string `base_digits` containing only the first `base` digits of `digits`.
3.  If `x` is less than the base, it simply returns the corresponding digit from `base_digits`.
4.  Otherwise, it enters a loop where it continuously appends the remainder of `x` divided by `base` to the result string, and then updates `x` to be the quotient of `x` divided by `base`. This process effectively converts `x` to the specified base.
5.  Finally, it returns the result string, which is the string representation of `x` in the specified base.

This function handles all possible inputs correctly and efficiently, as demonstrated by the test cases.