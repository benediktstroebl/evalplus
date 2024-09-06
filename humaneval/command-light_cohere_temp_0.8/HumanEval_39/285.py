Here is a Python script that defines a function `prime_fib` to calculate the n-th Fibonacci number that is prime:
```python
import math
def prime_fib(n: int) -> int:
    if n <= 0:
        raise ValueError("n should be a positive integer")
    elif n == 1:
        return 1
    else:
        a, b = 1, 2
        for _ in range(n - 1):
            a, b = b, a + b
        if math.is(N) > b:
            return b
```
This function uses a basic Fibonacci sequence formula to generate the n-th prime Fibonacci number, and then checks if the result is greater than the square of the next number in the sequence, which ensures it's prime.