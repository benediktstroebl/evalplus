Here's the solution:
```python
def prime_fib(n: int) -> int:
    if n <= 1:
        return n
    elif n <= 3:
        return 3
    else:
        # Using the Euclidean algorithm to find the largest prime factor and return n-squared
        sq = prime_fib(n-1) * 2
        while True:
            if sq <= n:
                n = sq
            else:
                sq -= n // sq
    return n
```
This code defines a recursive function `prime_fib` that computes and returns the n-th Fibonacci number that is also prime.  The function first checks if `n` is less than or equal to 1, in which case it returns `n`. It then checks if `n` is less than or equal to 3, returning 3. If `n` is greater than 3, it computes the square of the previous result (`prime_fib(n-1)`) multiplied by 2, and then enters a loop, using the Euclidean algorithm, to repeatedly subtract the greatest square divisor from `n` until it becomes less than or equal to the square of `prime_fib(n-1)`). The loop continues until the square becomes less than `n`, at which point `n` must be the largest prime factor of `n` and the loop terminates.