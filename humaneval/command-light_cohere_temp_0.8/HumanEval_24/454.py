```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n+1) if all(n% i == 0))
``` 
This code defines a Python function called largest_divisor that takes an integer n as input and returns the largest integer that evenly divides n, smaller than n. The function uses the interior iterator to loop through numbers from 1 to n+1. Then, it checks if all divisors of n are 0 using the all() function. Finally, the next method returns the number that satisfies the condition.