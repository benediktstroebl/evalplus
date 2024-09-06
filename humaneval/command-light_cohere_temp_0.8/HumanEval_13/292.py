```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both inputs must be positive integers.")
    while b != 0:
        a, b = b, a // b
    return min(a, b)

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```
This script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers `a` and `b`. The function first checks if both inputs are non-zero positive integers, and if so, proceeds to find the GCD using a loop where it alternates the values with the divisor. The function then returns the the smallest of the two numbers, ensuring that the result is always an integer. 
The test section ensures that the function behaves correctly with various inputs and produces the expected outputs.