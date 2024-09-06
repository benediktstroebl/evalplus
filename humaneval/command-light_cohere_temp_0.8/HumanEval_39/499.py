```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0:
        return 5
    prime_fib = 6
    while prime_fib <= n:
        if n % prime_fib == 0:
            return prime_fib
        prime_fib += 1
    return n
```
This code provides a function `prime_fib` that computes and returns the n-th Fibonacci number that is prime. It employs an loop to determine if the number is prime by checking if the number is divisible by any number up to 6. This function can be used to find the n-th Fibonacci prime in O(log n), which is an efficient way compared to other naive methods.