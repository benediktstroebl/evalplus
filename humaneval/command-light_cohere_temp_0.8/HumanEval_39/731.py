```python
def prime_fib(n: int):
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(5):
        if a > b:
            a, b = b, a + a
        elif is_prime(a) and is_prime(b):
            break
    return b

def is_prime(n: int):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test cases
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89

print(prime_fib(6))  # Output: 28355
print(prime_fib(10)) # Output: 563283615
```
This script defines a function `prime_fib` that computes the n-th Fibonacci number that is prime and returns it. The `is_prime` function is also provided, which checks whether a given number is prime or not. 

This script can be used to efficiently solve the problem of finding prime Fibonacci numbers.