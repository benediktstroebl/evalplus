Here is a Python script that defines a function, `largest_divisor`, which finds the largest integer that evenly divides a given number `n` without a remainder:
```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer that divides n evenly, 
    smaller than n.
    """
   
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    return n
```