```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of a and b must be non-zero")
    return max(x for x in range(1, min(a, b) + 1) if a % x == 0 and b % x == 0)

# Test cases
assert greatest_common_divisor(3, 5) == 1
assert greatest_common_divisor(25, 15) == 5
assert greatest_common_divisor(0, 5) == 0
assert greatest_common_divisor(50, 25) == 25
assert greatest_common_divisor(100, 50) == 50
```  This code defines a function `greatest_common_divisor` that computes the greatest common divisor of a and b. The code also provides several test cases to verify the correctness of the function.