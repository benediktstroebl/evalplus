```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of the inputs is zero.")
    if a == 0 or b == 0:
        return 0
    return max(d for d in range(1, min(a, b)) + 1 if a % d == 0 and b % d == 0)

if __name__ == "__main__":
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(6, 10) == 1
    assert greatest_common_divisor(0, 5) == 0
    assert greatest_common_divisor(8, 2) == 8
    assert greatest_common_divisor(15, 7) == 5
    assert greatest_common_divisor(10, 20) == 10
    assert greatest_common_divisor(50, 25) == 5
    assert greatest_common_divisor(30, 10) == 5
```
The code defines a function greatest_common_divisor that calculates the greatest common divisor of two integers a and b. It employs a test-range(1, min(a, b))+1 approach to find all divisors of min(a, b) while checking if both a and b are divisible by it, and it returns the greatest of these divisors as the result. The test suite ensures that the function correctly calculates the GCD of various input pairs.