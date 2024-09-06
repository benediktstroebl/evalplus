```python
def largest_divisor(n: int) -> int:
    return n // max(x for x in range(1, n+1) if x % n == 0)
```
We use the built-in function 'max' to find the largest number divisor. We use a particular loop that iterates from 1 to 'n' and checks if the current number x is divisible by n. We use the a max to find the largest divisor that meets this condition.