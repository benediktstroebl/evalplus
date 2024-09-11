### Is Prime Function
#### Python Script

```markdown
# is_prime.py
# Description: A function to check if a number is prime

def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:  # 1 and numbers less than 1 are not prime
        return False
    elif n <= 3:  # 2 and 3 are prime
        return True
    elif n % 2 == 0 or n % 3 == 0:  # If the number is divisible by 2 or 3, it is not prime
        return False
    i = 5
    while i * i <= n:  # Check divisibility up to the square root of the number
        if n % i == 0 or n % (i + 2) == 0:  # Check for divisibility by 6k ± 1
            return False
        i += 6
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

This script defines a function `is_prime` that checks if a given number `n` is prime. It uses a simple and efficient approach to check for primality, which is sufficient for large numbers. The function handles edge cases like numbers less than or equal to 1 and checks for divisibility up to the square root of the number. The script includes test cases to verify the function's correctness.