```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 6
    if n % 3 == 0:
        return 5
    if n % 5 == 0:
        return 5
    return prime_fib(n-6)

# test the function
print(prime_fib(5))
```