```python
def largest_divisor(n: int) -> int:
    """
    Return the largest number divisible by n that is less than n itself. 
    """
   
    positive integers.
    """
    factorize(n) is the largest integer that can be divided evenly by n without leaving a remainder, 
    and it is also less than n.

    Example:
    factorize(n) --> list(divisors) = list(x for x in range(1, n+1) if x evenly divides n)
    """
    factorize(n) --> list(divisors) = list(x for x in range(1, n+1) if x evenly divides n)
    divisors.length = len(divisors)
    if divisors:
        # Reversed list is used to avoid creating a new list object
        return divisors[-1]
    else:
        return n  # No divisors for n, so n itself is the largest divisor
```
This function will find the largest number less than n, that divides n evenly.