```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n+1) if n % i == 0)
``` 
This Python function returns the largest integer that evenly divides the given number without a remainder. It employs a efficient algorithm using a generator expression to iterate through numbers from 1 up and checks each against the given number to see if the condition is met.