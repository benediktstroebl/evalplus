```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0 or n % 3 == 0:
        return 5
    else:
        a, b = 6, 7
        for _ in range(n - 5):
            a, b = b, a + b
            if a % 2 == 0 or b % 2 == 0:
                break
        return a
``` 
Do you need anything else?