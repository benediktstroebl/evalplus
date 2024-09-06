```python
def largest_divisor(n: int) -> int:
    return n // max(1, n // k for k in range(1, int(n**0.25))
```
This function returns the largest number that evenly divides the given number 'n', smaller than 'n'. It uses the technique of finding the maximum number such that divides the given number exactly, and then divides it by the maximum divisor to ensure that the result is always greater than 0.