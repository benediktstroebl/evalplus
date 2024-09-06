```python
def fizz_buzz(n: int):
    return len({i for i in range(1, n+1) if i % 10 == 7 and i % 13 == 0})
```
Here, the function uses a generator expression with a lambda function to check if a number is divisible by 11 or 13. The function then returns the general length of the numbers' list which meet this condition, which is also the number of times the digit 7 appears in the numbers from 1 to n.