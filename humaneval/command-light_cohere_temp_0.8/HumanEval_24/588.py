Here's the self-contained Python script with a function that finds the largest divisor of a given number:

```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number that divides n evenly, 
    smaller than n
    """
    return next((i for i in range(1, n+1) if all(i% j == 0 for j in range(1, n))))
```
The function returns the largest number that evenly divides the given number, ensuring that the result is always an integer.