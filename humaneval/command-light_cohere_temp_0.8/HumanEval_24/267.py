```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if n % d == 0))
``` 
This code provides a function that returns the largest integer divisor of the given number n that is less than n itself. The code uses the smaller numbers first until the largest divisor is greater than the input number, which is guaranteed to be true due to the nature of divisibility rules.