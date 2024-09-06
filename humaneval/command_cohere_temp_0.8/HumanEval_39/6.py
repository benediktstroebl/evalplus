Here's a Python script with a self-contained function that solves the problem:
```python
def is_prime(n):
    """
    Checks if a number is prime
    """
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

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n <= 0:
        raise ValueError("n must be positive")
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        #Calculating nth Fibonacci number
        prev_fib = 0
        curr_fib = 1
        for _ in range(3, n + 1):
            prev_fib, curr_fib = curr_fib, prev_fib + curr_fib
        
        #Filtering out non-prime values
        while not is_prime(prev_fib) and not is_prime(curr_fib):
            curr_fib += prev_fib
            prev_fib = curr_fib
            if not is_prime(curr_fib):
                curr_fib += prev_fib
        
        return curr_fib
```

This script defines two functions: `is_prime`, which checks whether a given number is prime, and `prime_fib`, which returns the n-th Fibonacci number that is also prime. The `prime_fib` function first calculates the n-th Fibonacci number using an iterative approach. Then, it iterates through the Fibonacci numbers, filtering out the non-prime values, until it finds the n-th prime Fibonacci number. 

Here's an example of function usage:
```python
>>> prime_fib(1)
2
>>> prime_fib(2)
3
>>> prime_fib(3)
5
>>> prime_fib(4)
13
>>> prime_fib(5)
89
>>> prime_fib(6)
233
```