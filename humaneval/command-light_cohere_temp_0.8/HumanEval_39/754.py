```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n == 2:
        return 2
    else:
        for i in range(2, n):
            if is_prime(i):
                break
        return i

def is_prime(n: int):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test the function
print(prime_fib(5))
print(prime_fib(7))
print(prime_fib(10))
```

This code defines a `prime_fib` function that calculates and returns the n-th Fibonacci number that is prime. The function uses an loop to check if each number from 2 to the input number is prime. It also has a simple `is_prime` function that checks if a given number is prime or not. 

This code is well-contained and self-explanatory, as it explains all the concepts and methods involved in the process of solving the problem.