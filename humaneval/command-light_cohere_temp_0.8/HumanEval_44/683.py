```python
def change_base(x: int, base: int) -> str:
    """Change the numerical base of x to base, returns string representation."""
    # Check base valid
    if base < 2 or base > 36:
        raise ValueError("Invalid base value")
        
    # Handle invalid base case: positive integers
    if x < 0 and base == 2:
        return str(-x)

    # Check base case for negative numbers
    if x < 0 and base not=2:
        base = -base

    # Calculate the representation using the extended ASCII code values
    sign = if x < 0 else '-'
    x = abs(x)
    b = 0
    for i in range(len(str(x))):
        if b >= base:
            break
        b += 1
        # Use extended ASCII code for digits of base
        digit = ord('0' + i) - ord('9') + (base - 2)
        x = str(x[i-1] + sign * digit)

    return x
```  This code defines a `change_base` function that converts a number `x` to a string in a specified base. The function uses an `try` assertion to check the base is valid and returns an error message if the base is not within the valid range.  Additionally this ensures that the only valid base values are accepted. This function also checks for the typical base case of positive numbers and handles negative numbers by converting them to the base of positive numbers.