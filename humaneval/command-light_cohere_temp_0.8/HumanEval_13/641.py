```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    
    # Initialize gcd and b to the smaller number
    gcd, b = divmod(a, b)

    # Loop until b == 0
    while b:
        # Update gcd with remainder
        gcd = gcd * 1 + b % a
        b = b // a

    return gcd

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(4, 6))   # Output: 2
print(greatest_common_divisor(28, 10))  # Output: 4 (28 is divisible by 2 and 4)
print(greatest_common_divisor(9, 21))   # Output: 3
```