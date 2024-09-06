```python
def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    prev_fib, curr_fib = 0, 1
    for _ in range(n - 2):
        prev_fib, curr_fib = curr_fib, prev_fib + curr_fib
    
    return prev_fib if is_prime(prev_fib) else curr_fib if is_prime(curr_fib) else None
```

This script defines a function `prime_fib(n)` which aims to return the n-th number that is both a Fibonacci number and a prime number. The function handles edge cases by returning 2 for n=1, 3 for n=2, and None for negative values of n. To achieve this, it uses an optimized Fibonacci sequence calculation and a simple prime number checking function. 

To achieve the optimization, the function calculates the Fibonacci sequence by iterating through it using the formula `curr_fib = prev_fib` for `n` iterations, and then using `prev_fib + curr_fib` for the next iteration. This reduces the number of iterations and makes the calculation more efficient. 

Note, this solution uses a simple prime checking method to optimize performance. It checks for divisibility up to the square root of the number, which is enough for practical purposes. However, it isn't the most efficient prime checking method, but it provides a good balance between accuracy and computation speed.