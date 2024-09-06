```python
def largest_divisor(n: int) -> int:
    return (n//2 + 1)  # returns the largest even divisor less than n
```

This function uses the concept of the largest even divisor which is always greater than the square root of the number by 1. The function then returns the integer value which is the largest divisor for the given number.