### Prime Fibonacci Number Generator
#### Problem: Generate the n-th prime Fibonacci number

Here is a self-contained Python script that solves the problem using a generator function to lazily compute Fibonacci numbers and a helper function to check if a number is prime.

```markdown
### Code
```python
def is_prime(num: int) -> bool:
    """
    is_prime checks if a number is prime.
    
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


def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The index of the prime Fibonacci number to generate.
    
    Returns:
    int: The n-th prime Fibonacci number.
    """
    a, b = 0, 1
    count = 0
    while True:
        a, b = b, a + b
        if is_prime(b) and count == n:
            return b
        count += 1


# Example usage:
if __name__ == "__main__":
    for i in range(1, 6):
        print(f"prime_fib({i}) = {prime_fib(i)}")
```

### Explanation

*   The `is_prime` function checks if a number is prime by iterating up to the square root of the number and checking for divisibility.
*   The `prime_fib` function generates Fibonacci numbers on the fly and checks if each number is prime using the `is_prime` function. When the n-th prime Fibonacci number is found, it returns the number.
*   The example usage at the end demonstrates how to use the `prime_fib` function with indices 1 to 5.
"""

This script uses a generator to lazily compute Fibonacci numbers, which is more efficient than precomputing and storing all Fibonacci numbers up to a certain limit. This makes it suitable for generating prime Fibonacci numbers for large values of `n`.