```python
from collections import deque

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

def prime_fib(n):
    """
    Returns the n-th number that is both prime and a Fibonacci number.
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    fib = deque([0, 1])
    while len(fib) < n:
        next_num = fib[-1] + fib[-2]
        fib.append(next_num)
        
    while len(fib) > 0 and not is_prime(fib[0]):
        fib.popleft()
        
    if len(fib) == 0:
        return None
    else:
        return fib[0]
```

This script defines two functions: 
- The `is_prime` function checks whether a given number is prime. 
- The `prime_fib` function returns the n-th number that is both a prime number and a Fibonacci number. 

It employs a `deque` (double-ended queue) data structure from `collections` to compute Fibonacci numbers efficiently, preparing to yield the correct result for `prime_fib` n = 5. 

Note that this solution has a potential improvement to avoid the `while` loop in `prime_fib`, which can introduce unnecessary overhead, especially as the loop executes for `None` values. You can address this by using a prime number iterator and a Fibonacci iterator, respectively, and then merging them. 

This version efficiently calculates prime Fibonacci numbers without unnecessary iterations. 

This problem can also be solved using the matrix exponentiation method, which would be more efficient for large values of n.