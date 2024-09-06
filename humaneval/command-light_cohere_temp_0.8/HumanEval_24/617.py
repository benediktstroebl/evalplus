```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number that divides n evenly, 
    where the largest possible divisor is less than n
    """ 
    return math.floor(n //sqrt(n))
``` 
This function finds the largest divisor of a given number 'n' such that the divisor is less than the number.