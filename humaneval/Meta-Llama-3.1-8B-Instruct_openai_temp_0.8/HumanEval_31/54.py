Here's a Python function that checks whether a number is prime or not:

```markdown
### is_prime Function
```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.
    
    Parameters:
    n (int): The number to check for primality.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    if n <= 3:  # 2 and 3 are prime
        return True
    if n % 2 == 0 or n % 3 == 0:  # If the number is divisible by 2 or 3, it's not prime
        return False
    i = 5
    while i * i <= n:  # We only need to check up to the square root of n
        if n % i == 0 or n % (i + 2) == 0:  # Check for divisibility by 6k ± 1
            return False
        i += 6
    return True
```

### Example Use Cases
```python
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False
```
This function uses a few optimizations to improve performance:

* It returns False for numbers less than or equal to 1.
* It returns True for numbers 2 and 3.
* It checks for divisibility by 2 and 3 early on.
* It only checks up to the square root of n for divisibility by other numbers.
* It uses the "6k ± 1" method to check for divisibility by other numbers.