```python
def fizz_buzz(n: int):
    return len({d for d in range(10, n+1) if (n % 11 == 0 or n % 13 == 0) and d == 7})
```
This function counts the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13. The function uses a generator expression and the list comprehension to efficiently achieve this task.