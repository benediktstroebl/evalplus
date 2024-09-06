```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer dividing n evenly, smaller than n.
    """
   
    max(1, n // divisor(n))
    where divisor(n) = int(n**0.25)
    return max
```
The function uses the Euclidean algorithm to find the largest integer that evenly divides n. It starts by testing the max(1, n // divisor(n)) and iteratively adjusts the divisor until the condition holds.