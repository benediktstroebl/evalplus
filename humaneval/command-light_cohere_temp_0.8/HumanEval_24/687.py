```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n+1) if all(n % i == 0))
``` 
This code defines a function called largest_divisor, which takes an integer n as input and returns the largest integer that divides n exactly without a remainder. It uses the necessary to find this largest divisor, and the next function generates a list of divisors from 1 up to n, and uses the all() function to check if every divisor divides n evenly without a remainder.