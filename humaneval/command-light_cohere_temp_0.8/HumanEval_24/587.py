```python
def largest_divisor(n: int) -> int:
    return next(
        i for i in range(1, n+1) if any(d % i == 0 for d in (1, n-i, n))
    )
``` 
This Python function, `largest_divisor`, is designed to find the largest integer divisor of a given number 'n' that is less than or equal to the original number. It uses a process of iterating through numbers from 1 up, and checks each number's divisibility with respect to the given numbers from 1 to the original 'n'. The largest such divisor is returned, which guarantees that it divides the original number evenly without a remainder.