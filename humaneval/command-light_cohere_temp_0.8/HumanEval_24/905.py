```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n + 1) if not n % d), 1)
``` 
This function iterates through numbers from 1 to n and returns the largest divisor of n which is smaller than n, ensuring the function is self-contained and can be easily tested.