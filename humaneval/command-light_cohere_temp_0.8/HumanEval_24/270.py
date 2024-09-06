```python
def largest_divisor(n: int) -> int:
    """
    Return the largest number smaller than n that divides evenly.
    """
    # Approach:
    - We know that all numbers from 1 to n-1 divide n evenly
    - We select the largest among them
    - Return the largest divisor of n
    """
    return max(range(1, n+1), key=lambda i: i % n == 0)
```