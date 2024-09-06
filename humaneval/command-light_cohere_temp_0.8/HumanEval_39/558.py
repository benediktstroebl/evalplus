```python
import math
def prime_fib(n):
    if n <= 1:
        return n
    fib = 0
    prime = 2
    for i in range(2, n+1):
        if math.is_prime(prime):
            fib += prime
        prime += 1
    return fib
``` 
This Python function, prime_fib, calculates the nth Fibonacci number while ensuring it's also prime. The function starts by initializing the Fibonacci number to 0 and the next prime number to 2. It then iterates through range from 2 to n, and for each prime encountered, it adds that prime to the Fibonacci number. After the loop completes, it returns the calculated Fibonacci number.