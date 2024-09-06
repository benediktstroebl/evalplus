Here's the function to generate the n-th Fibonacci number and check if it is prime:
```python
import math
def prime_fib(n):
    if n <= 0:
        raise ValueError("n should be a positive integer")
    elif n == 1:
        return 2
    else:
        limit = int(math.sqrt(n)) + 1
        prev, curr = 2, 3
        for _ in range(limit):
            next_num = prev + curr
            if next_num <= n or (math.isprime(next_num) and n - next_num):
                prev, curr = curr, next_num
            else:
                break
        return curr
```

This code defines a Python function `prime_fib` that calculates and returns the n-th Fibonacci number. It employs a factorial method to generate the Fibonacci sequence and concurrently checks each number to determine if it is prime.

The function includes input validation to ensure `n` is a positive integer. It employs a `math.sqrt()` function to compute the square root of `n` and adds 1 to the result to handle the base case of `n` being 1. 

The loop iterates through the range of potential Fibonacci numbers and adds the next Fibonacci number to the sequence. It then checks whether the next number is less than `n` or passes the test for primality using `math.isprime()` function and only if the number is prime, or greater than `n`.