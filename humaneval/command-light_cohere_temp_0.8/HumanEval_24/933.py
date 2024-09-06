```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not n % d and divisible(n, d)), n)

def divisible(n: int, d: int) -> bool:
    return n % d == 0 and d <= n

def test_largest_divisor():
    assert largest_divisor(15) == 5
    assert largest_divisor(16) == 16
    assert largest_divisor(8) == 8
    assert largest_divisor(10) == 4
    assert largest_divisor(12) == 4
    assert largest_divisor(30) == 5
    assert largest_divisor(0) == 0
```
This code provides a function called `largest_divisor` that calculates the largest divisor of a given number `n`. The function uses a generator expression to find all divisors less than `n` that divide `n` without a remainder, and then returns `n` if no such divisors exist. The `divisible` function is used to test if a number is divisible by another number, and it returns `True` if the condition is met and `False` otherwise. The `test_largest_divisor` function tests the `largest_divisor` function with various input values.