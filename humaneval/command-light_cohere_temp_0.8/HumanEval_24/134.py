```python
def largest_divisor(n: int) -> int:
    return n // max(n, 1)
``` 
The above function uses the concept of the maximum value that can divide evenly given any number, and since 1 is always divisible by any number, the largest divisor is simply n divided by 1.