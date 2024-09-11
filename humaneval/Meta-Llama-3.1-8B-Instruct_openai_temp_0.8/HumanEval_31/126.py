```markdown
### Prime Number Checker

The following Python script checks whether a given number is prime or not.

#### Code

```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.
    
    Args:
        n (int): The number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:  # 0 and 1 are not prime numbers
        return False
    if n <= 3:  # 2 and 3 are prime numbers
        return True
    if n % 2 == 0 or n % 3 == 0:  # numbers divisible by 2 or 3 are not prime
        return False
    i = 5
    while i * i <= n:  # only need to check up to the square root of n
        if n % i == 0 or n % (i + 2) == 0:  # check for divisibility by 6k +/- 1
            return False
        i += 6
    return True

# Test cases
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False
```

#### Explanation

This script defines a function `is_prime` that takes a number `n` as input and returns `True` if it's prime, and `False` otherwise.

The function first handles the edge cases where `n` is less than or equal to 1 (not prime), or `n` is 2 or 3 (prime).

Then, it checks if `n` is divisible by 2 or 3, in which case it's not prime.

Next, it checks divisibility by 6k +/- 1 numbers up to the square root of `n` using a while loop. If `n` is divisible by any of these numbers, it's not prime.

If the function hasn't returned `False` by this point, it means `n` is prime, so it returns `True`.

The script then includes test cases to verify the correctness of the `is_prime` function.