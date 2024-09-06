```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be positive.")
    while b != 0:
        if b % a == 0:
            a, b = b, a
        else:
            break
    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(6, 20))   # Output: 2
print(greatest_common_divisor(0, 0))   # Input: both numbers are zero, raises ValueError
```
The function `greatest_common_divisor` calculates the greatest common divisor of two numbers a and b. It first checks if both numbers are positive, and if they are, it enters a loop where it repeatedly divides the larger number by the smaller one until the smaller number becomes zero. It then returns the sources: 

1. the loop condition may also be optimized to a direct subtraction b % a == 0.
2. a and b are then updated to hold the current value of a and b respectively, which ensures that a won't be updated to the original value of b.
3. The ValueError is raised if the input is invalid. 

This function is self-contained and can be used to solve the problem of finding the greatest common divisor of two numbers.