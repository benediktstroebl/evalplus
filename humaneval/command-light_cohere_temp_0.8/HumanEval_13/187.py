```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("One or both arguments cannot be zero")
    return max(d for d in range(1, min(a, b)) if a % d == 0 and b % d == 0)

# Example usage
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```
This code defines a function called greatest_common_divisor, which takes two integers a and b as input and returns the greatest common divisor of a and b. The function first checks if either a or both of the input arguments are zero, and if so, raises a ValueError. Then, the function uses the maximum function to find the largest integer divisor of the minimum of the two integers, which is the greatest common divisor.