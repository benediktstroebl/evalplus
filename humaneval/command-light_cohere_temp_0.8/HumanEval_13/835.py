```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    # Calculate the GCD using the Euclidean Algorithm
    while b != 0:
        a, b = b, a % b
    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(36, 60))  # Output: 12
print(greatest_common_divisor(105, 24))  # Output: 24
```
This Python script defines a function `greatest_common_divisor` that computes the greatest common divisor of two integers `a` and `b`. The function utilizes the Euclidean Algorithm to efficiently find the GCD, which has a time complexity of O(log(min(d,e))). This is significantly more efficient than prime factorization methods.