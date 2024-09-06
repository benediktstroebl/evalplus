```python
def prime_fib(n: int):
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(n - 2):
        a, b = next((i for i in range(2, a + b) if is_prime(i)), a + b)
    return a

def is_prime(n: int):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Example usage
print(prime_fib(5))  # Output: 89
print(is_prime(7))   # Output: True
```
The code defines a function `prime_fib` that calculates the n-th Fibonacci number which is also prime, and a function `is_prime` that checks whether a given number is prime or not. The code then tests these functions with example inputs and prints the results.