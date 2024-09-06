```python
def prime_fib(n: int):
    """
    Returns n-th Fibonacci number and is also prime
    Returns a prime number if it's true, otherwise returns Fibonacci number
    """
    if n <= 1:
        return n
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    for i in range(5, n + 1, 6):
        if i % 2 == 0 or i % 3 == 0:
            continue
        else:
            break
    return i
```
This code defines a function 'prime_fib(n)' that calculates the n-th Fibonacci number and returns it, or returns a prime number if it's found. If the input n is greater than 1, the function will return the n-th Fibonacci number. If n is divisible by 2 or 3, it will directly return 2 or 3, respectively, since those numbers are prime and also their divisors. If n is greater than 5, 6, or any multiple of 5, it will start checking for divisibility by 2 and 3, incrementing by 6 until a prime is found, or it will return the largest prime less than n.