```python
def change_base(x: int, base: int) -> str:
    """
    Convert input number x to base base using conversion
    rules.
    Args:
        - integer x,
        - integer base
    Returns:
        - string representation in the chosen base
    """
    if x < 0:
        raise ValueError("Input number should be non-negative")
    elif base < 2 or base > 36:
        raise ValueError("Base should be between 2 and 36")
        
    num = str(x)
    reversed_digits = '0123456789'
    len_num = len(num)
    
    if base == 2:
        # Use the reverse of digits to achieve binary representation
        base_digits = reversed_digits[:len_num]
        return base_digits
    
    elif base == 10:
        # Use standard decimal digits
        base_digits = reversed_digits[:len_num]
        return base_digits
    
    else:
        # Convert the number into a string of length base-length digits
        num_str = ''.join(int(c) for c in num)
        return num_str[:base]

# Unit tests
test_change_base = []
test_change_base.push(8(change_base(8, 2)))
test_change_base.push(change_base(-8, 2))
test_change_base.push(change_base(7, 2))
test_change_base.push(change_base(0, 10))
test_change_base.push(change_base(1, 10))
test_change_base.push(change_base(35, 10))
test_change_base.push(change_base(23, 10))
test_change_base.push(change_base(1234, 2))
test_change_base.push(change_base(10, 10))
test_change_base.push(change_base(10, 36))
test_change_base.push(change_base(-10, 10))
```