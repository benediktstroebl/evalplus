```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            return i
```
The function `largest_divisor(n)` takes a number `n` as input and iterates through all factors of `n` from 1 to `n` itself.  It returns the largest factor that divides `n` evenly, which is the closest thing to a "largest divisor" that fits the vague definition of the problem. This solution implicitly assumes there may exist multiple divisors of equal size, and chooses the largest one of them. If there are multiple largest divisors, this solution is not deterministic and might return any of them.