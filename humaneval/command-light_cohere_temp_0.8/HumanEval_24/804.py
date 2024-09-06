Here's a self-contained Python script that defines a function `largest_divisor(n)` which finds the largest divisor of the number n:
```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number that divides n evenly, 
    smaller than n.
    """
    for i in range(1,int(n**0.5)+1):
        while n % i == 0:
        return i
    return -1
```