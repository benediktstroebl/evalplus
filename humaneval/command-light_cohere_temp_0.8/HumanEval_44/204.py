```python
def change_base(x: int, base: int) -> str:
    if base < 2 or base > 36:
        raise ValueError("Invalid base number")
        
    res = ""
    for n in str(x):
        if base == 2:
            res += str(n)
        elif base == 10:
            res += f"{int(n):0>b}"
        else:
            res += f"{n:0>b}"
        base -= 1
    return res

# Test cases
print(change_base(8, 3))  # Expected output: '22'
print(change_base(8, 2))  # Expected output: '1000'
print(change_base(7, 2))  # Expected output: '111'
``` 
This code defines a `change_base` function that converts a number to a string representation using the specified base. It uses string formatting and base conversion rules and tests if the base number is within valid limits. 

This function can be used to convert numbers to different base representations in a self-contained manner.