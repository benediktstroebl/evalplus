```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1,  math.
    def __name__ = 'gcd'
def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    return gcd(b, a % b)

# Unit tests
def test_largest_divisor():
    assert largest_divisor(1) == 1
    assert largest_divisor(2) == 2
    assert largest_divisor(3) == 3
    assert largest_divisor(4) == 4
    assert largest_divisor(5) == 5
    assert largest_divisor(10) == 5
    assert largest_divisor(15) == 5

# Example usage
print(largest_divisor(15))
```
This code defines a function `largest_divisor(n)` that returns the largest divisor of the number `n`. It uses the `gcd` function to calculate the greatest common divisor of `n - 1` and the smallest prime number that is less than `n`. The `test_largest_divisor` function contains unit tests that verify the correctness of the `largest_divisor` function.