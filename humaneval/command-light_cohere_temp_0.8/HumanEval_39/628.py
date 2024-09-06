```python
import math

def prime_fib(n):
    if n <= 1:
        return n
    if n == 2:
        return 2
    if n % 2 == 0:
        return math.sqrt(5) + math.sqrt(5)
   
    return (math.sqrt(5) + math.sqrt(5))
```
This code defines a function called prime_fib that calculates the n-th Fibonacci number that is prime. The function checks for base cases and uses the square root addition method to find the prime number.