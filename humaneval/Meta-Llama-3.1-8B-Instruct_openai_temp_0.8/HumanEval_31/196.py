### Prime Number Checker
#### Description
A Python function to check if a given number is prime or not.

#### Code
```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        # Numbers less than or equal to 1 are not prime
        return False
    elif n <= 3:
        # 2 and 3 are prime
        return True
    elif n % 2 == 0 or n % 3 == 0:
        # Numbers that are multiples of 2 or 3 are not prime
        return False
    i = 5
    while i * i <= n:
        # Check for factors up to the square root of n
        if n % i == 0 or n % (i + 2) == 0:
            # Numbers that have factors other than 1 and themselves are not prime
            return False
        i += 6
    return True

# Example usage
if __name__ == "__main__":
    print(is_prime(6))   # False
    print(is_prime(101)) # True
    print(is_prime(11))  # True
    print(is_prime(13441)) # True
    print(is_prime(61))   # True
    print(is_prime(4))    # False
    print(is_prime(1))    # False
```

#### Explanation
This function checks if a given number `n` is prime by first handling the base cases where `n` is less than or equal to 1, or `n` is 2 or 3. It then checks if `n` is divisible by 2 or 3, and if so, returns False.

Next, it checks for factors of `n` up to the square root of `n` by incrementing `i` by 6 each time (since all primes are of the form 6k ± 1, for some integer k). If `n` is divisible by any of these factors, the function returns False.

If none of the above conditions are met, the function returns True, indicating that `n` is prime.