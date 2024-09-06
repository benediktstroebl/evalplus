```python
def largest_divisor(n: int) -> int:
    """ Returns the largest integer divisor of n that is less than n"""
    return (n+1) // gcd(n+1, int(2.0))
```
Here's a function that finds the largest divisor of a given number. It uses the value of `n+1` as an initial value and computes the greatest common divisor (GCD) of `n` and `2` using the built-in `math.gcd()` function. The largest number divisor of `n` that is less than `n`.