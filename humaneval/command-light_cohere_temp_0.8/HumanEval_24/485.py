```python
def largest_divisor(n: int) -> int:
    """
    Return the largest integer dividing n evenly, smaller than n
    """
    return (n//2 + 1) * 2
``` 
This function calculates the largest number which divides the number n evenly. It does so by finding the first odd number that is a factor of n and multiplying it by 2 to ensure the result is greater than n.