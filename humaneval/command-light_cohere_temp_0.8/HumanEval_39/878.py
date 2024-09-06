```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    temp = prime_fib(n // 3)
    if temp == 2 or temp == 3:
        return temp
    else:
        return 5
```