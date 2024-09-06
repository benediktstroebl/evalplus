```python
def prime_fib(n: int):
    """
    Returns the n-th Fibonacci number and verifies if it's prime.
    This uses sieve of Eratosthen for prime testing
    """
    # Initialize Fibonacci sequence
    a, b = 0, 1
    sequence = [a, b]

    # Create an list of prime numbers less than or equal to n
    primes = [i for i in range(2, n + 1) if is_prime(i)]

    # Use the list comprehension to get the n-th Fibonacci number
    nth_fib = [sequence[i] for i in primes]

    # Create a list of potential divisors for nth_fib
    potential_divisors = [i for i in range(1, n + 1) if nth_fib[i] != 1 and i != nth_fib[i]]

    # Use the Sieve of Eratosthenes to find all prime divisors
    divisors = [i for i in potential_divisors if is_prime(i)]

    return nth_fib[0] if len(divisors) == 0 else nth_fib[0] // divisors[0]

def is_prime(n: int):
    """
    Returns True if n is a prime number, False otherwise.
    """
    sieve of Eratosthen with only 1 and n.

def main():
    """
    Driver function to test the above functions.
    """
    test = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10
    }

    for test_num, expected in test:
        actual = prime_fib(test_num)
        print(f"{test_num} should be {expected}, but is {actual}")
        assert actual == expected

```

This Python script defines a function `prime_fib` that calculates the n-th Fibonacci number and determines if it is prime. It also employs the prime testing with the Sieve of Eratosthenes to efficiently determine the prime divisors of the Fibonacci number. The `main` function serves as the driver function, passing test cases and asserting the correctness of the `prime_fib` function for each test case.