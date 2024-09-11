### Prime Number Checker
#### Python Implementation

```markdown
### Code
```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    A prime number is a positive integer that is divisible only by itself and 1.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if n is prime, False otherwise.

    Examples:
        >>> is_prime(6)
        False
        >>> is_prime(101)
        True
        >>> is_prime(11)
        True
        >>> is_prime(13441)
        True
        >>> is_prime(61)
        True
        >>> is_prime(4)
        False
        >>> is_prime(1)
        False
    """
    if n <= 1:
        # Numbers less than or equal to 1 are not prime
        return False
    for i in range(2, int(n ** 0.5) + 1):
        # Check divisibility up to the square root of n
        if n % i == 0:
            # If n is divisible by any number, it's not prime
            return False
    # If n is not divisible by any number, it's prime
    return True
```

### Example Use Cases

```markdown
### Usage
```python
# Check if a number is prime
print(is_prime(101))  # Output: True
print(is_prime(6))    # Output: False

# Check for large prime numbers
print(is_prime(13441))  # Output: True
```
```