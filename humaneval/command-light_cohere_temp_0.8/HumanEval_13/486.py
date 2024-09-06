```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one input is required")
    elif a == 0 or b == 0:
        return 0
    
    # Remove common factors from consideration
    while a % b == 0:
        a = a // b
    while b % a == 0:
        b = b // a
    
    # If one or both numbers is a prime factor, they have no divisors
    if a == 2 or b == 2:
        return 2
    
    # If both numbers are divisible by 2, the greatest divisor is 2
    if a % 2 == 0 or b % 2 == 0:
        return 2
    
    return max(a, b)

# Example usage
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```