```python
def largest_divisor(n: int) -> int:
    return n // max(x for x in range(1, n+1) if x % n == 0)
```
We use the 'max' function to find the largest number which is divisible by all numbers from 1 to n, ensuring the largest divisor less than n.