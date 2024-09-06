```python
def largest_divisor(n: int) -> int:
    return (n//2 + 1)  # return the next larger divisor than n divided by 2
```
This function uses the concept of the next larger divisor than the number n, by taking the remainder away from n divided by 2 and adding 1.

It effectively finds the largest divisor that divides the number evenly and smaller than n.