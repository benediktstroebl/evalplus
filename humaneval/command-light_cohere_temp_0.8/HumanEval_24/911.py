```python
def largest_divisor(n: int) -> int:
    return n // max(x for x in range(1, n+1) if x % n == 0)
``` 
This Python function, `largest_divisor`, calculates the largest integer that evenly divides a given number `n`. It utilizes a list comprehension to find all divisors of `n` less than or equal to the number itself, and then takes the maximum of these values.