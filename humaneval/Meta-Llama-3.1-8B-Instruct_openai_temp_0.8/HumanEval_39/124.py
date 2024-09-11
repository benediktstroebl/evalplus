### Fibonacci Prime Number Generator
#### A Python Script to Find the N-th Fibonacci Prime Number

Below is a Python function that generates the n-th Fibonacci prime number.

```markdown
```python
import math


def is_prime(num: int) -> bool:
    """
    Checks if a number is prime.
    
    Args:
    num: The number to check.
    
    Returns:
    True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def fibonacci_prime(n: int):
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n: The position of the Fibonacci prime number to find.
    
    Returns:
    The n-th Fibonacci prime number.
    """
    fib_num = 0
    fib_next = 1
    prime_num = 0
    counter = 0
    while counter < n:
        # Generate the next Fibonacci number
        fib_num, fib_next = fib_next, fib_num + fib_next
        # Check if the Fibonacci number is prime
        if is_prime(fib_num):
            prime_num = fib_num
            counter += 1
    return prime_num


# Example usage
if __name__ == "__main__":
    for i in range(1, 6):
        print(f"The {i}-th Fibonacci prime number is {fibonacci_prime(i)}")
```

### Explanation
This script uses a helper function `is_prime` to check if a number is prime. It then uses another function `fibonacci_prime` to generate the n-th Fibonacci prime number.

The `fibonacci_prime` function generates Fibonacci numbers on the fly and checks each one to see if it's prime using the `is_prime` function. It keeps track of the n-th prime Fibonacci number found and returns it.

### Note
The `is_prime` function uses a simple trial division method to check for primality, which is sufficient for small integers. For larger integers, you may want to use a more efficient primality test.