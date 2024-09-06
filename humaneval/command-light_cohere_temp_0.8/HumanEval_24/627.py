```python
def largest_divisor(n: int) -> int:
    return next((x for x in range(1, n+1) if not any(n % x == 0)))
```
This function takes an integer n as input and returns the largest integer that evenly divides n, smaller than n. It uses the Python's next() function to generate the sequence of integers from 1 to n, and the if statement to check whether any of these integers divide n evenly. The first element that satisfies this condition. 

This function is self-contained and efficiently solves the problem of finding the largest divisor of a given number n.