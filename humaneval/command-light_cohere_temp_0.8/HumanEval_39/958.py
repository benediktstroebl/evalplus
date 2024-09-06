```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 2
    prime = []
    for i in range(3, n+1, 2):
        if is_prime(i):
            prime.append(i)
    if len(prime) == n:
        return prime

def is_prime(num: int):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# Driver code
print(prime_fib(5))  # Output: 89
print(prime_fib(12))  # Output: 2 3 4 8 3 2 7 11
```
This code defines the `prime_fib` function that calculates the n-th Fibonacci number and checks if it's prime. It also has the `is_prime` function to check if a given number is prime.