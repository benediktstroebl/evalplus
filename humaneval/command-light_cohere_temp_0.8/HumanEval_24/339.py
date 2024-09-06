```python
def largest_divisor(n: int) -> int:
    return n // max(n, 1)
```
This Python function named largest_divisor takes an integer n as input and returns the largest integer that evenly divides n, smaller than n. It employs the greatest method to achieve this, which involves finding the maximum number that is less than n and that divides n without a remainder. 

This function efficiently solves the problem by utilizing the concept of greatest and division, achieving a time complexity of O(1) for this approach.