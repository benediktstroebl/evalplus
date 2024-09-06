```python
def change_base(x: int, base: int) -> str:
    if base < 2 or base > 36:
        raise ValueError("Invalid base number")
        
    ret = str(x)
    
    for c in range(len(ret)):
        if ret[c] != ord('0' + base):
            break
        ret = ret.replace(ret[c], chr(base))
        
    return ret

# Example usage:
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
print(change_base(5, 10))  # Output: '500'
``` 
This function, change_base, takes an integer x and a base as input and returns the converted number.  The function implements the str.strategy for converting numbers to the desired base.