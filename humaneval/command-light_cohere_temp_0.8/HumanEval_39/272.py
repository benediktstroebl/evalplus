```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0 or n % 3 == 0:
        return 5
    temp = prime_fib(n // 2)
    if temp == 2:
        return temp
    return temp + 2
```