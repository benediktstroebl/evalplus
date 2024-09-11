```python
def change_base(x: int, base: int) -> str:
    """
    Change numerical base of input number x to base.
    Args:
        x (int): Number to be converted.
        base (int): Target numerical base (less than 10).
    
    Returns:
        str: String representation of x after conversion to base.
    """
    if x == 0:
        return '0'
    
    digits = "0123456789"
    if x < base:
        return digits[x]
    
    result = ""
    while x > 0:
        result = digits[x % base] + result
        x //= base
    
    return result

# Test cases
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```
This script defines the function `change_base` that converts a given number `x` from decimal to a specified base `base`. It recursively calculates the remainders of `x` divided by `base` and prepends these remainders to the result string in reverse order. If `x` is less than `base`, it directly returns the corresponding digit. The script includes test cases to demonstrate its correctness.