```python
import math
def prime_fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n <= 3:
        return n
    co = 2
    for i in range(2, n + 2):
        if math.isq(co, i) == 0:
            co = i
    return co
``` 
This script defines a function `prime_fib` that calculates the n-th Fibonacci number that is prime and returns it as the result. 

Here, the function starts with a simple check to ensure that the input n is a positive integer. If it's not, it raises a `ValueError`. If n is 1, the function returns 2 (the first Fibonacci number) as this is also a prime. 

Then, a for loop is used to iterate from 2 up to n. The reason is that the numbers from 2 to n are factors of the (n+1)th number, and we want to find the largest one that is prime. 
Finally, the function returns the n-th Fibonacci number that is prime.