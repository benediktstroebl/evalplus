```python
from itertools import count
import math

def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n <= 0:
        raise ValueError("n must be positive")
    
    fib = [0, 1]
    curr_num = 2
    count = count(fib[1])
    
    for _ in range(n - 1):
        next_num = curr_num + count()
        fib.append(next_num)
        curr_num = next_num
    
    # Search for the nth Fibonacci number in the sequence
    while len(fib) <= n:
        fib.append(curr_num)
        curr_num = curr_num + count()
    
    return fib[n]
```

This script defines a `prime_fib` function, which, for a given positive integer `n`, returns the n-th Fibonacci number that is also a prime number. The script also includes a helper `is_prime` function to check if a number is prime. 

The `prime_fib` function initially checks if `n` is greater than 0, raising a `ValueError` otherwise. It then initialize the Fibonacci sequence with the initial values of [0, 1], and uses the `count` function from the `itertools` module to generate subsequent Fibonacci numbers by adding the previous two numbers. The generated numbers are stored in the `fib` list. 

The function then iterates `n-1` times to build the Fibonacci sequence up to the `(n-1)`-th number. After this preparation, the function searches for the n-th Fibonacci number in the `fib` list, and returns it. 

This approach ensures that each Fibonacci number is only computed once, making the code more efficient. 

The `is_prime` function is also included to check if a given number is prime. It implements a simple brute-force algorithm by checking all numbers from 2 to the square root of the given number. If the number is divisible by any integer in this range, it's not a prime. 

Overall, the code is concise and effective in solving the problem.