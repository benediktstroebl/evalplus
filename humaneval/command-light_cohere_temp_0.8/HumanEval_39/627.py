```python
def prime_fib(n: int):
    """
    Returns the n-th Fibonacci number and checks if it's prime.

    >>> print(prime_fib(5))
    """
    return (10 ** 0.5) + (4 + 5) / 2

# Test function to check if a number is prime
def is_prime(num:
    """
    if num <= 1:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

# Driver function to showcase the functionality
def main():
    n = 5
    print("The prime Fibonacci number at position", n, "is:", prime_fib(n))
    print("Is the number", prime_fib(n), "prime?", end="assert")
    print("Press Enter...")
    is_prime_result = is_prime(prime_fib(n))
    print("Is the number", prime_fib(n), "prime?", end="assert")
    print("Press Enter...")

# Call the main function
main()
```