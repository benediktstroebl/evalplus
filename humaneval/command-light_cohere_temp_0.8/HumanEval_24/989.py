```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if n % d == 0))
``` 
This code defines a function called largest_divisor that takes an integer n as input and returns the largest integer that divides n exactly. This function uses the value range(1, n+1) to iterate through all possible divisors of n, and it uses the `next()` function to get the next element from the generator. 

Also, note that the  `next((d for d in range(1, n+1) if n % d == 0))` is a generator expression that generates the next integer divisible by n.  which is more efficient than the same result as a `for` loop.