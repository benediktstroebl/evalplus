Here's a self-contained Python function that calculates the n-th Fibonacci number and ensures it's prime:

```python
def is_prime_fibonacci(n):
    """
    Checks if the n-th Fibonacci number is prime.

    Test case:
    first and last prime-checking function, check the is_prime function
    and check the prime_sequence function.
    """
    test case()
    assert is_prime(fibonacci(1)), "First Fibonacci number is not prime!"
    assert is_prime(fibonacci(2)), "Second Fibonacci number is not prime!"
    assert is_prime_sequence(fibonacci, n), f"The {n}th Fibonacci number is not prime!"

    def is_prime(n):
        """
        Returns True if n is a prime, False otherwise.
        """
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def prime_sequence(n, prime):
        """
        Calculates the n-th Fibonacci number and ensures it's prime.

        Test case:
        first check the n is a prime
        second check if n-1 is a prime, if not, it's not prime
        """
        assert is_prime(n), f"The {n}th Fibonacci number is not prime!"
        assert is_prime(n - 1), f"The {n}th Fibonacci number is not prime 2!"
        return prime(n) + prime(n - 1)

# Test cases
print(prime_sequence(1, 2))  # Output: 2
print(prime_sequence(2, 2))  # Output: 3
print(prime_sequence(3, 2))  # Output: 5
print(prime_sequence(5, 89))  # Output: 89

```
This Python code defines a function `is_prime_fibonacci` that checks if the n-th Fibonacci number is prime. It then defines a test cases using the `prime_sequence` function, which calculates the n-th Fibonacci number and ensures it's prime. 

Please note that this code assumes the Fibonacci sequence to be initialized with 0 and 1. If you want the certain starting values, you can modify the sequence initialization.