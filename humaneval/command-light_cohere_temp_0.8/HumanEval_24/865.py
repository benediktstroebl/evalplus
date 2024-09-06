```python
def largest_divisor(n: int) -> int:
    """ Returns the largest number which divides the given number evenly"""
    return next((i for i in range(1, n+1) if n % i == 0))
``` 
This code provides a self-contained solution for finding the largest divisor of a given number.