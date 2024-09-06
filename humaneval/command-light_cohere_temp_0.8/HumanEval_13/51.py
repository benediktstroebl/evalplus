```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    return max(d for d in range(1, max(a, b)) if a % d == 0 and b % d == 0)

# Example usage:
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
``` 
This script defines a function `greatest_common_divisor(a, b)` that calculates the greatest common divisor of two integers `a` and `b`. It uses a list comprehension to find the largest integer `d` such that both `a` and `b` are divisible by `d`, and then returns the greatest common divisor. 
 test cases are provided to ensure the correctness of the function.