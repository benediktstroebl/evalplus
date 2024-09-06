```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not n % d and divisible(n, d)), n)

def divisible(n: int, d: int) -> bool:
    return n % d == 0 and d <= n

def test_largest_divisor():
    assert largest_divisor(15) == 5

def test_divisible():
    assert not divisible(15, 5)
```
This code defines a function `largest_divisor(n)` that returns the largest integer dividing the given number without a remainder, ensuring that it's less than the input number. The `divisible(n, d)` function checks whether a divisor `d` can divide `n` without a remainder. The `test_largest_divisor()` and `test_divisible()` functions are used to run the function with the given tests and assert the results.

I hope this helps you solve the problem!