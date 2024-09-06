```python
def fizz_buzz(n: int):
    return 7 - sum(1 for digit in str(n) if digit == 7 and n % 11 == 0 or n % 13 == 0)
```
The function counts the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.