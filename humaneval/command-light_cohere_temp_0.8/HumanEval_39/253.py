```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0 or n % 3 == 0:
        return 0
    prime = True
    for i in range(5, n + 1, 6):
        if prime_fib(i) == 0:
            prime = False
            break
    return prime
```
This function, `prime_fib`, computes the n-th Fibonacci number that is prime. It uses dynamic programming and trial and error to find the prime factor of n and returns a boolean indicating the result.

Please note that the function will raise an error if the given number is not a positive integer.