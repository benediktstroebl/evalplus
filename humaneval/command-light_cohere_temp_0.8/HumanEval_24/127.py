```python
def largest_divisor(n: int) -> int:
    """
    Return the largest integer dividing n evenly, 
    excluding n itself.
    """
    number from 1 to n-1 are all divisors, 
    except when they are equal to n
    """
    return max((i for i in range(1, n+1) if n % i == 0)) + 1
```