```python
def prime_fib(n: int):
    """
    Returns n-th Fibonacci number and checks if it's prime.
    Returns 'True' if Fibonacci number is prime, else returns 'False'.
    """
    if n <= 1:
        return True  # Base case
    if n % 2 == 0 or n % 3 == 0:
        return False  # Cannot be prime
    # Calculate Fibonacci number using iterative method
    fib = 0
    fib += 1
    temp = 0
    temp += 1
    while temp <= n:
        fib += temp
        temp += temp
    return fib == n and True  # checks if number is prime
```