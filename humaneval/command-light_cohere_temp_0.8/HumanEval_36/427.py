```python
def fizz_buzz(n: int) -> int:
    return sum([x == 7 for x in range(1, n + 1) if x % 15 == 7])
```
We calculate the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.