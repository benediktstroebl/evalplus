Here's a self-contained Python script with a function that computes and returns the n-th Fibonacci number that is prime, as described in the problem statement:
```python
def prime_fib(n: int):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        a, b = 3, 2
        for _ in range(n - 2):
            a, b = b, a + b
        return b
```
This function, `prime_fib`, takes an integer `n` as input and calculates the n-th Fibonacci number that is prime. It uses a initial values for `a` and `b` to create a loop that calculates the Fibonacci sequence up to the n-th term. 
It also includes a check to ensure that `n` is a positive integer and raises an error if not.