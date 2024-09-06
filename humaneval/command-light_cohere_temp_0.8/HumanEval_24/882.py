```python
def largest_divisor(n: int) -> int:
    """
    Finds the largest integer which divides the given number evenly, 
    and returns its value.
    """
    In the the factorizes, and primes into consideration, 
    the function returns the largest number that satisfies the condition.
    """
example usage:
    >>> largest_divisor(15)
    5
    """
    # use induction to find the factorial representation
    # of the given number
    # for example 15 = 3 * 5
    # largest_divisor(3) = 3
    # largest_divisor(5) = 5
    # therefore, the largest divisor of 15 is 5
    return max(x for x in range(1, n+1) if n % x == 0)
```