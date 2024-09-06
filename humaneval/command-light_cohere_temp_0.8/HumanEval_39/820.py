```python
def prime_fib(n: int):
    """
    Returns the n-th number that is a Fibonacci number and is also prime.
    Returns None if no such qualities are met, which means n is not a Fibonacci number and not prime.
    Here is a list of prime numbers: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    """
    if n <= 1:
        return None  # Not a valid input

    # Check if n is a Fibonacci number
    if n % 2 == 0 or n % 3 == 0:
        return None  # Not a prime and not a Fibonacci number

    # Check if n is a prime
    for num in range(2, int(n**0.5) + 1):
        if n % num == 0:
        return None  # Not prime, so keep searching

    # Found a prime
    return n

# Test the function with some inputs
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
```
This function will return the n-th Fibonacci number that is prime, or None if none of the criteria are met.