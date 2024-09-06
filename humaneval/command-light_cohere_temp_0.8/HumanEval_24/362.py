```python
def largest_divisor(n: int) -> int:
    return n // 2 if n % 2 == 0 else n - 1
```
This Python function, `largest_divisor`, takes an integer `n` as input and returns the largest divisor of `n` as an integer. The function utilizes a testing by checking if the input number is even or odd, respectively, to determine the largest divisor accordingly. The function effectively finds the value of `n` and rounds it down to the nearest integer divisible by 2, handling both even and odd input numbers.