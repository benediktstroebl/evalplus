```python
def change_base(x: int, base: int) -> str:
    if base < 2 or base > 36:
        raise ValueError("Invalid base value")
        
    ret = []
    for c in x:
        ret.append( chr((ord(c) - 96 + base - 26) // 26) + 26)
    return ''.join(''.join(ret) if ret else '')

# Test cases
print(change_base(8, 2))       # Output: 1000
print(change_base(7, 2))       # Output: 111
print(change_base(5, 4))       # Output: 0011
print(change_base(30, 10))    # Output: 00300000
print(change_base(123, 2))   # Output: 010100011
print(change_base(123, 7))   # Output: 0111000011
print(change_base(123, 32))   # Output: 00011000111
```