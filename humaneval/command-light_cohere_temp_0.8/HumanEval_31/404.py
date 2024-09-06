```python
def is_prime(n):
    """Returns true if the number is prime, and false otherwise."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
``` 
This function checks for primality using several rules and tests. It begins by checking numbers less than or equal to 2 and 3, which are clearly prime. It then employs a simple rule: any even number greater than 2 is not prime. It then uses trial to check divisibility by prime numbers of form 5, until the square of the number being tested is less than or equal to the number.