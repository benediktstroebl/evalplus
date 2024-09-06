```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of the inputs must be a non-zero integer")
    return max(divisor(a) for divisor in [1, ..., a // b])

def divisor(n):
    return [i for i in range(1, n + 1) if n % i == 0]

# Unit tests
def test GreatestCommonDivisor():
    a = 3
    b = 5
    assert greatest_common_divisor(a, b) == 1
    a = 25
    b = 15
    assert greatest_common_divisor(a, b) == 5

if __name__ == "__main__":
    test GreatestCommonDivisor()
```
This Python code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers a and b. The function utilizes a helper function `divisor` to generate all divisors of n, and then returns the largest divisor found in the list. The main test function tests the greatest_common_divisor with different inputs and asserts that the function is working correctly. The code also provides an main block that runs the unit tests to ensure the correctness of the `greatest_common_divisor` function.