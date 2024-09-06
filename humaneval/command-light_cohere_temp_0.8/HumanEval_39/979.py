```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0 or n % 3 == 0:
        return 5
    if n % 5 == 0:
        return 13
    return prime_fib(n - 6)

# Example usage
print(prime_fib(5))
```