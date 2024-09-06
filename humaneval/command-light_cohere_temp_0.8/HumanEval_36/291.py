```python
def fizz_buzz(n: int) -> int:
    return sum(1 for d in range(10) if (n < 7) or (d % 11 == 0) or (d % 13 == 0))
```

This code defines a Python function `fizz_buzz` that calculates the number of times the digit 7 appears in integers less than `n` that are divisible by 11 or 13. It uses a constant loops and boolean conditions to achieve this. The function returns the number of such times 7 appears.