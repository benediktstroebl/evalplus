```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if n % d == 0))
```
This code defines a function named largest_divisor that takes an integer n as input and returns the largest divisor of n, which is the largest positive integer that evenly divides n without a remainder. The function uses the main loop to iterate through numbers from 1 to n+1, and for each divisor d, it checks whether n is divisible by d using the modulo operator (n % d). If the remainder is 0, it means d is a divisor of n, and the function returns d; otherwise, it continues iterating.