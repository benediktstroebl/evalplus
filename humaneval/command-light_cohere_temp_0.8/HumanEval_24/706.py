```python
def largest_divisor(n: int) -> int:
    return n // max([1] + n % k for k in range(2, int(n**0.5)))
```
This code defines a function `largest_divisor` that calculates the largest integer that divides a given number evenly. The function employs a principle of trial and error: starting from the smallest prime number 1, it adds the remainder of the number divided by each prime number to the list of divisors to find the largest one.