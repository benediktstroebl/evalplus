```python
def prime_fib(n: int):
    """
    Returns n-th number that is a Fibonacci number and is also prime.
    >>> prime_fib(1)
    2
    is_prime = True  # Initialize is_prime flag as True
    3
    is_prime = False  # Assume not prime
    4
    is_prime = True  # Check if the number is prime

    # Calculate Fibonacci numbers
    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    fib.append(0)  # Include a 0 as the last number in the list

    # Find the n-th Fibonacci number that is prime
    for i in range(len(fib)):
        if fib[i] == fib[i - 1] and is_prime:
            return fib[i]
    else:
        return None
```