### change_base.py
```markdown
# Change numerical base of input number to base.
# Return string representation after the conversion.
# base numbers are less than 10.

def decimal_to_base(x: int, base: int):
    """Convert decimal number to a specific base.
    
    Args:
        x (int): The decimal number to convert.
        base (int): The target base for conversion.
        
    Returns:
        str: The string representation of the input number in the target base.
    """
    if x < base:
        return str(x)
    else:
        return decimal_to_base(x // base, base) + str(x % base)


def change_base(x: int, base: int):
    """Change numerical base of input number to base.
    
    Args:
        x (int): The input number to convert.
        base (int): The target base for conversion.
        
    Returns:
        str: The string representation of the input number in the target base.
    """
    return decimal_to_base(x, base)


# Test cases
if __name__ == "__main__":
    print(change_base(8, 3))  # '22'
    print(change_base(8, 2))  # '1000'
    print(change_base(7, 2))  # '111'
```
This script defines a recursive function `decimal_to_base` to convert a decimal number to a specific base. The function `change_base` uses `decimal_to_base` to achieve the conversion. The script includes test cases to verify the correctness of the implementation.