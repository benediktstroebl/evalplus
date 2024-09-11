### Fibonacci Prime Generator
```python
def is_prime(num: int) -> bool:
    """
    Checks if a number is prime.

    Args:
    num (int): The number to check for primality.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def fibonacci_prime(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the Fibonacci prime to find.

    Returns:
    int: The n-th Fibonacci prime number.
    """
    a, b = 0, 1
    count = 0
    while True:
        if is_prime(b):
            count += 1
            if count == n:
                return b
        a, b = b, a + b


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the Fibonacci prime to find.

    Returns:
    int: The n-th Fibonacci prime number.
    """
    return fibonacci_prime(n)


# Example usage
if __name__ == "__main__":
    import unittest

    class TestFibonacciPrime(unittest.TestCase):
        def test_prime_fib(self):
            self.assertEqual(prime_fib(1), 2)
            self.assertEqual(prime_fib(2), 3)
            self.assertEqual(prime_fib(3), 5)
            self.assertEqual(prime_fib(4), 13)
            self.assertEqual(prime_fib(5), 89)

    unittest.main(argv=[__file__])
```

In this script, we first define a helper function `is_prime` to check if a number is prime. Then, we define the `fibonacci_prime` function to generate Fibonacci numbers and check if they are prime. The `prime_fib` function simply calls `fibonacci_prime` with the given position. We also include some example tests at the end to ensure the correctness of the `prime_fib` function.