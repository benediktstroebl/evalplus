```python
def largest_divisor(n: int) -> int:
    return n // max([i for i in range(1, n+1) if n % i == 0])
```
The above code defines a function `largest_divisor` which, given an integer `n`, finds the largest integer which divides `n` evenly (i.e., without leaving a priority, that is, smaller than n.  This result is useful for checking the size of divisors of a number, which can be used in many situations, such as calculating the remaining digits of a number in a certain base.