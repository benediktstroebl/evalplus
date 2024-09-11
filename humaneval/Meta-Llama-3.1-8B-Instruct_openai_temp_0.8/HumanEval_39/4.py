### Fibonacci Prime Finder
#### A Python Script to Find the N-th Fibonacci Prime Number
```python
def is_prime(num: int) -> bool:
    """
    Helper function to check if a number is prime.
    
    Args:
    num: The number to check for primality.
    
    Returns:
    True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def fibonacci_primes(n: int) -> int:
    """
    Returns the n-th Fibonacci number that is also prime.
    
    Args:
    n: The position of the Fibonacci prime to find.
    
    Returns:
    The n-th Fibonacci prime number.
    """
    a, b = 0, 1
    num_primes = 0
    while True:
        # Generate the next Fibonacci number
        a, b = b, a + b
        # Check if the Fibonacci number is prime
        if is_prime(b):
            num_primes += 1
            # Return the n-th Fibonacci prime if found
            if num_primes == n:
                return b


# Test the function
if __name__ == "__main__":
    print(fibonacci_primes(1))  # Output: 2
    print(fibonacci_primes(2))  # Output: 3
    print(fibonacci_primes(3))  # Output: 5
    print(fibonacci_primes(4))  # Output: 13
    print(fibonacci_primes(5))  # Output: 89
```
This script uses a helper function `is_prime` to check if a number is prime, and the main function `fibonacci_primes` to generate Fibonacci numbers and check if they are prime. It keeps generating Fibonacci numbers until it finds the n-th prime one.