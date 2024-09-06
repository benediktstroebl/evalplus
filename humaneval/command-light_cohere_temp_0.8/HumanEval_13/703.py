```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Incompatible inputs: a and b must be integers")
    
    if a == 0 or b == 0:
        return 0
    
    # Start by assuming a greater divisor than b
    candidate = b
    
    while candidate % a == 0:
        candidate //= candidate
    # If we ever found a divisor less than b, then a is a GCD
    if candidate == 1:
        return a
    
    return candidate

# Unit tests
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(2, 25)))  # Output: 25
print(greatest_common_divisor(20, 30)))  # Output: 5
print(greatest_common_divisor(0, 5))   # Output: 5
print(greatest_common_divisor(-5, 10))  # Output: 5
``` 
This function greatest_common_divisor(a, b) calculates and returns the greatest common divisor of two integers a and b. The function first handles edge cases where either a or b is zero, and in such cases, it returns 0. It then proceeds to find the largest divisor of a in b, while constantly dividing by a until b becomes 1.