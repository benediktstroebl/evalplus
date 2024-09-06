```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n <= 3:
        return 3
    else:
        m = n - 2
        i = 3
        while i * i <= m:
            if m % i == 0:
                m //= i
            else:
                i += 1
        return m

# Test the function
print(prime_fib(5))
```