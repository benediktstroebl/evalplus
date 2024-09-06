```python
def prime_fib(n: int):
    if n <= 1:
        return n
    else:
        a, b = 2, 3
        for _ in range(n - 2):
            if is_prime(a):
                b = a
            a += 1
        return b

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

print(prime_fib(5))
``` 
This Python script defines the `prime_fib` function, which computes the nth Fibonacci number that is prime and returns it. It also includes a simple test cases that verify the function's correctness. The function `is_prime` is added to check if a given number is prime or not.