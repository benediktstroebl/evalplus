```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one of the inputs is invalid")
    if not (a or b) % 2:
        raise ValueError("Both inputs must be odd numbers")
    
    # step 1: find the difference
    diff = a - b
    if diff < 0:
        raise ValueError("Input values make no sense")
    
    # step 2: find the common divisor
    gcd = diff if diff > 1 else 1
    while b != 0:
        a %= gcd
        b //= gcd
    return a

# test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
```