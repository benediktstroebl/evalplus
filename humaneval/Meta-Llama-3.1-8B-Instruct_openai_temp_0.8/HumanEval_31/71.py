### Prime Number Checker
#### Description
This script defines a function `is_prime(n)` that checks whether a given number `n` is prime or not. A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

#### Code
```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        # Numbers less than or equal to 1 are not prime
        return False
    for i in range(2, int(n**0.5) + 1):
        # Check if n has any divisors other than 1 and itself
        if n % i == 0:
            return False
    # If no divisors were found, n is prime
    return True


# Test cases
if __name__ == "__main__":
    print(is_prime(6))  # False
    print(is_prime(101))  # True
    print(is_prime(11))  # True
    print(is_prime(13441))  # True
    print(is_prime(61))  # True
    print(is_prime(4))  # False
    print(is_prime(1))  # False
```

#### Explanation
The `is_prime(n)` function takes an integer `n` as input and returns a boolean value indicating whether `n` is prime or not. Here's a step-by-step breakdown of the function:

1.  If `n` is less than or equal to 1, it is not prime, so the function returns `False`.
2.  The function iterates from 2 to the square root of `n` (inclusive) to check for divisors.
3.  If `n` is divisible by any number `i` in this range, it is not prime, so the function returns `False`.
4.  If no divisors are found, `n` is prime, so the function returns `True`.

Note that this implementation uses a trial division approach, which is sufficient for small to moderate-sized inputs. For larger inputs, more efficient algorithms like the Miller-Rabin primality test may be necessary.