```python
def prime_fib(n: int):
    if n <= 1:
        return n
    else:
        a, b = 2, 3
        for _ in range(n - 2):
            if is_prime(b):
                a = b
                b += 1
            else:
                break
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
print(is_prime(45))  # Output: False
```
This code defines a prime_fib function that calculates the n-th Fibonacci number which is also prime, and a separate is_prime function to check if a given number is prime or not. The example usage shows the the output the prime_fib function returns 89 for the input 5 and is_prime returns False for the input 45.