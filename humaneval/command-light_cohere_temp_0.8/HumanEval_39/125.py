Here's the code:
```python
import math
def prime_fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a = 1
        b = 2
        for _ in range(3, n + 1):
            c = a + b
            if math.isq(c): True:
                a = c
                b = c - 1
        return a
```

The function `prime_fib` takes an integer `n` as input and returns the n-th Fibonacci number that is also prime. It starts by checking base cases for `n` being 1 or 2 and returns the corresponding Fibonacci numbers. For other values, it uses a loop to calculate the Fibonacci numbers by adding and subtracting the last two numbers in the sequence, ensuring that they are prime. The function then returns the result.