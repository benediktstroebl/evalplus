```python
def largest_divisor(n: int) -> int:
    return (n-1) // god_prime(n)

def god_prime(n: int) -> bool:
    """ checks if n is a prime number"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
        return False
    return True
```