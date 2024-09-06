```python
def largest_divisor(n: int) -> int:
    return n // max(n, 1)

# Test case
assertEqual(largest_divisor(15), 5)
``` 
This code defines a function largest_divisor that calculates the largest integer that divides a given number n evenly. It uses the process involving the general formulas, specifically, the return value is the largest divisor less than n.