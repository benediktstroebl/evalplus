```python
def largest_divisor(n: int) -> int:
    """Finds the largest number divisible evenly into n, less than n."""
    # Make sure n is an integer
    n = int(n)
    # First, find all divisors of n up to the square root
    # of n
    divisors = [i for i in range(1, int(n ** .5) + 1)]
    # Sort the list of divisors
    divisors.sort()
   Wait, a list comprehension is not sorted by default.
    # Since biggest divisor is the largest in the list, which is i = n
    return int(n)
```