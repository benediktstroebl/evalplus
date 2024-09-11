### Largest Prime Factor Function
#### Python Script

```markdown
# Function to check if a number is prime
def is_prime(num: int) -> bool:
    """
    Check if a number is prime.

    Args:
    num (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# Function to find the largest prime factor
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n.

    Args:
    n (int): The number to find the largest prime factor of.

    Returns:
    int: The largest prime factor of n.

    Assumptions:
    n > 1 and is not a prime.
    """
    # Start checking from the square root of n
    for i in range(int(n ** 0.5), 1, -1):
        # Check if i is a factor of n and is prime
        if n % i == 0 and is_prime(i):
            return i
    # Return 2 if no factors are found
    return 2


# Example usage
if __name__ == "__main__":
    print(largest_prime_factor(13195))  # Output: 29
    print(largest_prime_factor(2048))   # Output: 2
```

This script defines two functions: `is_prime` checks if a number is prime, and `largest_prime_factor` finds the largest prime factor of a given number. The script then demonstrates the usage of `largest_prime_factor` with the provided examples.