```python
def largest_divisor(n: int) -> int:
    return int(math.sqrt(n))  # Returns the larger number that can divide n exactly, but larger than n.

```  This solution efficiently finds the largest divisor using the fact that the sqrt function returns the largest integer that divides n exactly without a remainder.