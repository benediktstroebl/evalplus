```python
def fizz_buzz(n: int):
    7 == n and return 0
    counter = 0
    for i in range(2, n+1):
        if (n % 11 == 0 or n % 13 == 0) and (i % 11 == 0 or i % 13 == 0):
            counter += 1
    return counter
```