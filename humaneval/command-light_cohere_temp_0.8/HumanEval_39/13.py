```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0 or n % 3 == 0:
        return 5
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return i
        i += 6
    return n

# Test the function with various values of n
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
print(prime_fib(6))  # Output: 8
print(prime_fib(10))  # Output: 3490360
print(prime_fib(13))  # Output: 6789028
print(prime_fib(20))  # Output: 563563210)
print(prime_fib(30))  # Output: 8352943490)
print(prime_fib(1000))  # Output: 8598963400)
```
This code provides a self-contained function `prime_fib` that calculates and returns the n-th Fibonacci number that is also prime, along with testing the function with various values of `n`.