Here is a Python script with a self-contained function that solves the problem of finding the n-th Fibonacci number that is also prime:

```python
import math
def prime_fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # Check if the n-th Fibonacci number is prime
        sqrt_n = int(math.sqrt(n)) + 1
        sqrt_n_prime = 2**(sqrt_n) + 1
        for i in range(2, sqrt_n_prime):
            if sqrt_n_prime_pow2 + i * i % sqrt_n_prime == 0:
                continue
            else:
                break
        return sqrt_n_prime
```
The function `prime_fib` takes an integer `n` as input and returns the n-th Fibonacci number that is also prime. The function first checks if `n` is a positive integer, and if not, raises a `ValueError`. Then, it checks if `n` is 1 or 2, and if so, returns the corresponding Fibonacci number. If `n for n` greater than 2, the function calculates the square root of `n` and initializes a counter `sqrt_n_prime` to 0. Then, it iterates from 2 to the square root of `sqrt_n_prime` and checks if the square of the product of `i` and `sqrt_n_prime` is divisible by `sqrt_n_prime`. If so, the loop continues; otherwise, the loop breaks and the corresponding Fibonacci number is returned.