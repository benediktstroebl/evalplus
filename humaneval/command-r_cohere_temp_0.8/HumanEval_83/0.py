```python
def starts_one_ends(n):
    """
    Count the numbers of n-digit positive integers that start or end with 1.
    """
    # Starting with 1
    count = 9**n
    # Ending with 1
    count += 10**n - 11**n
    
    return count
```