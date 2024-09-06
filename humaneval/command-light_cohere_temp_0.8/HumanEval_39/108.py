```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0 or n % 3 == 0:
        return 5
    # check for other prime factors
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return i
        i += 6
    return n

# test suite for function
print(prime_fib(5))
print(prime_fib(6))
print(prime_fib(7))
print(prime_fib(10))
```

This code defines a function `prime_fib` that returns the n-th Fibonacci number that is prime. The function first checks for numbers less than or equal to 1 and returns that number. Then, it checks for other prime factors of the remaining numbers up to the square root of n. The function then returns n if no other prime factors are found.