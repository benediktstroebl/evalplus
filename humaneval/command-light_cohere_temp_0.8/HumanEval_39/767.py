```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0 or n % 3 == 0:
        return 5
    return prime_fib(n-1) + 2
``` 
This function is a recursive implementation of the Fibonacci sequence that is also prime. It starts with base cases for `n=1`, `n=2`, and `n=3`, and then uses the conditional check to determine if the current number is prime or not, and recursively calls itself to find the next number in the sequence.