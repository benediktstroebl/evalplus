```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 6
    for i in range(5, n + 1, 2):
        if is_prime(i):
            return i
    return n

def is_prime(n: int):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
        return False
    return True

# Example usage
print(prime_fib(5))
print(is_prime(6))
```

This code defines a function `prime_fib` that computes the n-th Fibonacci number that is also prime and returns it. The function uses a same number's previous prime test to determine if it is prime or not. The function also uses an simple for loop to iterate through numbers from 5 up to `n`.  and checks if any of those numbers are prime.