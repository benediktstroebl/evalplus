```python
import math
def prime_fib(n):
    if n <= 0:
        raise ValueError("n should be a positive integer")
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        limit = int(math.sqrt(n)) + 1
        prime_fib_loop = [2]
        for _ in range(limit):
            if prime_fib_loop[len(prime_fib_loop) - 1 >= n:
                break
            prime_fib_loop.append(prime_fib_loop[len(prime_fib_loop) - 1])
        prime_fib_loop.append(math.sqrt(prime_fib_loop[-1]) + 1)
        return prime_fib_loop[-1]
```
The function uses a loop to generate all possible Fibonacci numbers and checks if each one is prime. The function returns the final number of the loop if it is a prime, otherwise it returns None.