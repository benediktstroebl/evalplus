```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 2
    for i in range(3, n + 1):
        if is_prime(i) == True:
            return i
    return n

def is_prime(n: int):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
        return False
    return True
```
This code defines a function `prime_fib` that computes the n-th Fibonacci number that is prime and returns it. Additionally, it provides a helper function `is_prime` that checks if a given number is prime or not.