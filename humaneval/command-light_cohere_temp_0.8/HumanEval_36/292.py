```python
def fizz_buzz(n: int):
    return len({c for c in str(n) if c == 7 and n % 11 == 0 or n % 13 == 0})
```
This function counts the number of times the digit 7 appears in the string representation of numbers less than n which are divisible by 11 or 13. The function returns the volume of suchs.