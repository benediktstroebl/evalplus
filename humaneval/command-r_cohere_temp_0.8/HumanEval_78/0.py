```python
def is_prime(num):
    """Check if number num is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num ** (1/2)) + 1):
        if num % i == 0:
            return False
    return True

def hex_key(hex_str):
    """Count prime hexadecimal digits in hex_str."""
    primes = 0
    for digit in hex_str:
        if digit in '2357BD':
            primes += 1
    return primes
```