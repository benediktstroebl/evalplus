```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not n % d))
``` 
This function will provide the largest number that evenly divides the number n, smaller than n, using the built-in `range()` function and a generator expression.