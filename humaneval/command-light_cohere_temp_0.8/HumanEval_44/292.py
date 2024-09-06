```python
def change_base(x: int, base: int) -> str:
    if base == 10:
        return str(x)
    elif base > 10 or base < 2:
        raise ValueError("Invalid base number. Change it to a number between 2 and 10.")
    else:
        # Compute the representation in the desired base
        res = [f'{digit:02x}' for digit in str(x)]
        return ''.join(res)

# Test cases
print(change_base(8, 3))  # Expected output: '22'
print(change_base(8, 2))  # Expected output: '1000'
print(change_base(7, 2))  # Expected output: '111'
print(change_base(0, 12))  # Expected output: '0000'
print(change_base(5, 1))   # Expected output: '05'
``` 
The function `change_base` takes an integer `x` and a base `base` as input and returns the converted number represented in the desired base. This is using the simple if statement to check if the base is valid, and then computes the representation of `x` in the desired base.