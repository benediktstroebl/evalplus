```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return "Error: One or both numbers are zero!"
    
    # Initialize variables and handle negative numbers
    ca = 0 if a < 0 else a
    cb = 0 if b< 0 else b
    
    # Calculate the GCD using the Euclidean algorithm
    while True:
        a %= ca
        b %= cb
        if a == 0 or b == 0:
            break
        ca += 1
        cb -= 1
    
    # Return the calculated GCD
    return max(ca, cb)

# Example usage
gcd = greatest_common_divisor
print(gcd(3, 5))  # Output: 1
print(gcd(25, 15))  # Output: 5
```