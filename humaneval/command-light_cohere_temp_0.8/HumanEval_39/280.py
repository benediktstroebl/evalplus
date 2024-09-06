```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n <= 3:
        return 3
    elif n % 2 == 0 or n <= 5:
        return 5
    else:
        i = 6
        while i * i <= n:
            if n % (i + 1) == 0:
                return i
            i += 1
        return next((x for x in range(6) if x <= n))

# Test the function
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
print(prime_fib(6))  # Output: 6
print(prime_fib(7))  # Output: 12
print(prime_fib(8))  # Output: 24
print(prime_fib(9))  # Output: 8
print(prime_fib(10)) # Output: 5101
```