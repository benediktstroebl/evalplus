```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n + 1) if n % d == 0))
``` 
This code defines a function `largest_divisor` that takes an integer `n` as input and returns the largest integer that divides evenly into `n`. The function uses a list comprehension to iterate through numbers from 1 to `n+1`, and checks if the number divides `n` evenly (i.e., the  The code achieves this by using the built-in function `next()` which returns the next value in the iterator, and applies the condition to check divisibility. 
This function is self-contained, efficient, and straightforward, making it a good choice for solving this specific problem.