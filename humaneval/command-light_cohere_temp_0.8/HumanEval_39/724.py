```python
import math
def prime_fib(n):
    if n <= 0:
        raise ValueError("n should be a positive integer")
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        limit = int(math.sqrt(n)) + 1
        for i in range(3, limit):
            if math.isprime(i):
                yield i
        else:
            continue
    return iter(reversed(prime_fib(n)))
``` 
This function takes an integer n as input and returns an iterator yielding the n-th Fibonacci number that is prime. It does this by iterating through the first three Fibonacci numbers (2, 3, 5) and checking whether each number is prime using the math.isprime function from if it's prime, it yields that number and repeats this process until it finds a non-prime number.