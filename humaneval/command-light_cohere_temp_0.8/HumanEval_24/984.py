```python
def largest_divisor(n: int) -> int:
    return int(2) ** max(x for x in range(1, n + 1) if n % x == 0)
``` 
This function determines the largest number that divides the input number (n) evenly, smaller than n. It employs the use of the simplest approach, checking each divisor up to the input value and identifying the maximum value. 

This function is self-contained and uses simple logic to solve the problem.