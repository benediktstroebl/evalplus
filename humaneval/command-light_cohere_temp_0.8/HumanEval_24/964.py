```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer dividing n evenly, smaller than n
    """
    return next((d for d in range(1, int(n**0.25)) if n % d == 0)
``` 
This function employs the `next` function and a loop to traverse through the numbers from 1 up until the one that yields a remainder of 0 when divided with n. This effectively finds the more integers that divide evenly into n than the largest one, which is n / 1.