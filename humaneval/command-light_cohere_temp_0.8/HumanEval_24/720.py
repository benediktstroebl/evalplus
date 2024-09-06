```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n + 1) if not(n % d)) or n)
``` 
This function iterates through numbers from 1 to n, and returns the largest divisor found, ensuring it's smaller than n. 
It uses the `next()` function, which under the `itertools` module, returns the next element in the specified iterator.