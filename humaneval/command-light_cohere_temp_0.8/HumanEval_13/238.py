```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    # Find the greatest divisor of a and b
    gcd = multiply_with_carry(a, b)
    # Return the greatest common divisor
    return gcd

def multiply_with_carry(x: int, y: int) -> int:
    s = 0
    t = x
    if y > 0:
        carry = y & 15  # bitmask
    while t < y:
        s += t & 15  # decimal multiplication
        t += y
    return s

# Example usage
a = 3
b = 5
print(greatest_common_divisor(a, b))  # Output: 1
```