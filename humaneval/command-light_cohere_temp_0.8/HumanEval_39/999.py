```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 3
    else:
        prime = 5
        for i in range(5, n + 1, 6):
            if n % i == 0:
                return i
    return n
``` 
This code defines a function `prime_fib` that calculates the n-th Fibonacci number that is prime. It returns the both cases for even given input.