```python
import math
def prime_fib(n):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    elif n % 2 == 0:
        return 5
    else:
        temp = prime_fib(math.sqrt(n) -n // 2)
        return temp + 2
``` 
This code defines a function `prime_fib` that calculates the n-th Fibonacci number that is prime and also it is also the n-th number. It uses a mathematical knowledge to find the prime factor of the square root of n and then adds 2 to get the next Fibonacci number.