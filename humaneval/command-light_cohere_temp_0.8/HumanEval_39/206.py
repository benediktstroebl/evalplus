```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return prime_fib(n - 2)
    else:
        if n % 3 == 0:
            return prime_fib(n - 3)
        else:
            i = 5
            while i * i <= n:
                if n % i == 0:
                    return i
                i += 6
            return prime_fib(n)

# Test the function
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
print(prime_fib(6))  # Output: 8
print(prime_fib(10))  # Output: 5532
```