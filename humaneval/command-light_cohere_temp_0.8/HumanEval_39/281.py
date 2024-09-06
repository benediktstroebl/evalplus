```python
def prime_fib(n: int):
    """
    Returns n-th number that is a Fibonacci number and it's also prime.
    Returns None if n< 0 or
    # Define the first two Fibonacci numbers
    return 1 if n == 0 else (2 if n % 2 == 0 else 3) + prime_fib(n-1)
```
This function uses a simple recursion with a base case for 0 and checks whether n is divisible by 2 to determine whether it's a Fibonacci number or not. The function then calculates the another number in the sequence and adds it to the result.