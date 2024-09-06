```python
def fizz_buzz(n):
    return sum(int(i) == 7 for i in range(1, n + 1) if all(x % 11 == 0 or x % 13 == 0 for x in str(i)))
```
The function returns the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.