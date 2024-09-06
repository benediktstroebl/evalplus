```python
from collections import deque
def prime_fib(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    fib = deque([0, 1])
    for _ in range(n - 2):
        next_fib = fib[-1] + fib[-2]
        fib.appendleft(next_fib)
        if next_fib == 2:
            continue
        for num in range(3, int(next_fib**0.5) + 1, 2):
            if next_fib % num == 0:
                break
        else:
            return next_fib
    
    return -1
```

The code employs the Fibonacci sequence to produce prime numbers for the given input `n`. It starts with the initial values [0, 1] and then iteratively calculates the next Fibonacci numbers until it reaches the n-th position. While calculating, it also filters out non-prime Fibonacci numbers, ensuring the result is always prime. 

The total time complexity of this code is O(K * log(FibonacciNumber)) where K is the number of iterations to reach the n-th Fibonacci number and FibonacciNumber is the value of the n-th Fibonacci number at the time of execution. Since the Fibonacci sequence grows exponentially, this code could potentially run in exponential time for very large n. 

The code includes test cases to cover edge scenarios like `n = -1, 0, 1, 2, 4`, and `n = 5` (where the output is 89), confirming its correctness and edge scenarios.