```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, int('inf')))

def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    return gcd(b % a, a)

# Unit tests
def test_largest_divisor():
    assert largest_divisor(15) == 5
    assert largest_divisor(20) == 4
    assert largest_divisor(12) == 4
    assert largest_divisor(8) == 2
    assert largest_divisor(3) == 3
    assert largest_divisor(1) == 1
```

This Python code provides a function `largest_divisor(n)` that returns the largest integer that evenly divides `n`, ensuring that the result is less than n. The function uses the smaller prime factors of n are calculated using the `gcd` function, which returns the greatest common divisor of a and b. The `test_largest_divisor` function contains unit tests to ensure the correctness of the `largest_divisor` function.