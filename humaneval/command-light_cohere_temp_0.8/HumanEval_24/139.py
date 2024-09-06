```python
def largest_divisor(n: int) -> int:
    return n // max(x for x in range(1, n+1) if n % x == 0)
```
This Python code defines a function `largest_divisor` that calculates the largest divisor of a given integer `n`. 

The function utilizes a list comprehension to find all factors of numbers from 1 to `n`, and then returns the largest number among them that evenly divides `n`. 

This self-contained function provides an efficient way to find the largest divisor of a given number, ensuring the solution is quick and easy to understand.