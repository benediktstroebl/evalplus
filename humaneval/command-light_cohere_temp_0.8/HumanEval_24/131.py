```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n + 1) if all(j == i % j for j in range(1, n + 1)))
``` 
This function returns the largest integer that evenly divides the given number, smaller than the number itself. 

Please note that this implementation uses the 'next' function with a generator expression to efficiently iterate through all divisors until the given number, ensuring that it only considers factors that are smaller than the target.