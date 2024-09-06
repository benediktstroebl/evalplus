```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if n % d == 0))
``` 
This function will find the largest number that evenly divides the given number 'n', without returning a negative number.