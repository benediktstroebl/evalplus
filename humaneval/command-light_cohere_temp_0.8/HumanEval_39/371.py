```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n <= 3:
        return 3
    elif n % 2 == 0:
        return 5
    else:
        six = 6
        for i in range(6, n + 1, 6):
            if n % i == 0:
                return i
        else:
            return n
```