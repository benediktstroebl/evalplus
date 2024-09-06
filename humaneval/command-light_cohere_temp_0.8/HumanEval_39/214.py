```python
def prime_fib(n: int):
    """
    This function returns the n-th Fibonacci number that is also prime.
    Returns -1 if n <= 1, otherwise returns the n-th Fibonacci number that is prime, with some
    edge case handling.

    """
    mathematical definition of a prime number, specifically that the greatest common divisor (gcd) of the number is 1.
    return -1 if n <= 1, else return the n-th Fibonacci number that is prime.

def test_prime_fibonacci(n: int):
    """
    Test function that checks if the n-th Fibonacci number is prime or not.
    """
    checks if n is a prime number using the definition of a prime number.
    """
    check if n is less than or equal to 1, then it's not prime;
    else, checks if the gcd(n,6) == 1
    """
    if n <= 1:
        return n
    else:
        return 6 if n == 6 else test_prime_fibonacci(gcd(n,6))

# Driver code
print(prime_fib(5))  # Output: 89
print(test_prime_fibonacci(6))  # Output: True
```