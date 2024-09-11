### Prime Number Check
#### Python Script

```markdown
### Code
```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    Parameters:
    n (int): The number to check for primality.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n <= 1:  # numbers less than or equal to 1 are not prime
        return False
    if n == 2:  # 2 is the only even prime number
        return True
    if n % 2 == 0:  # even numbers are not prime
        return False
    i = 3
    while i * i <= n:  # only need to check odd factors up to the square root
        if n % i == 0:  # if the number is divisible, it's not prime
            return False
        i += 2  # increment by 2 to check only odd numbers
    return True  # if no divisors found, the number is prime

### Example Usage
print(is_prime(6))   # False
print(is_prime(101)) # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))   # True
print(is_prime(4))    # False
print(is_prime(1))    # False
```

### Explanation
This script defines a function `is_prime(n)` that checks whether a given number `n` is prime or not. It uses a loop to check for divisibility by odd numbers up to the square root of `n`, and returns `True` if no divisors are found and `False` otherwise. The function also handles edge cases such as numbers less than or equal to 1, which are not prime.

### Example Use Cases
The script includes example usage of the `is_prime(n)` function with various inputs, demonstrating its correctness.