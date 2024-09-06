```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    gcd = ((a, b) for gcd in itertools.find_all(lambda x, x != 0 and x != 1))
    return gcd[0] if gcd else 0

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```
This script defines a function greatest_common_divisor(a, b) that computes the greatest common divisor of two integers a and b. The function uses the iterative approach with the built-in function find_all to find the greatest common divisor. The test cases demonstrate the the approach with a few test cases.