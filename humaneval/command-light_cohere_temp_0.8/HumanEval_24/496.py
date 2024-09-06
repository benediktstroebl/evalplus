```python
def largest_divisor(n: int) -> int:
    return n // 2 if n % 2 == 0 else n + 1
```
This Python function, `largest_divisor`, takes an integer `n` as input and returns the largest divisor of `n` (the largest number that divides `n` evenly). It uses the `return n // 2 if n % 2 == 0` to handle the case of even numbers, and returns `n + 1` for odd numbers. 
This function is self-contained and efficiently solves the problem of finding the largest divisor of a given number.