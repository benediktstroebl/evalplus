```python
def largest_divisor(n: int) -> int:
    """
    Return the largest number that divides n exactly and is smaller than n
    """
    return int((n + 1) // (2 * 1.5))
``` 
The above function returns the largest number which divides the given number n exactly and is smaller than n.