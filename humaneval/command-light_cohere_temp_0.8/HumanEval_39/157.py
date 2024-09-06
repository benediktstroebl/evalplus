```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0 or n % 3 == 0:
        return 0
    is_prime = True
    for i in range(5, int(n**0.5) + 1, :
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        return n
return None
```