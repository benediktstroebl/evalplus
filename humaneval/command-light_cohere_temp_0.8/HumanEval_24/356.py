```python
def largest_divisor(n: int) -> int:
    return n // max(1, n // i for i in range(2, int(n**0.5)))
``` 
This code defines a Python function `largest_divisor` that calculates the largest number that divides a given number `n` evenly, smaller than `n`. The function uses the concept of finding the maximum divisor less than n and divides n by the maximum divisor to get the largest divisor that evenly divides n.