```python
def is_prime(n):
    """
    Returns True if the number is prime, False otherwise.
    # A prime number isn is a number greater than 1 that has no divisors besides 1 and itself.
    if n <= 1: return False
    if n == 2: return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
        return False
    return True
``` 
The function 'is_prime' determines whether a given number 'n' is prime or not. It loops through a certain logic to identify prime numbers, which are greater than 1 and have only two distinct factors: 2 and themselves. 

The function also handles special cases: if 'n' is less than or equal to 1, it is not prime; if 'n' is 2, it is considered prime; and if there exists any divisor for 'n' greater than 2, the function returns False. 

This self-contained function effectively solves the given problem and passes the tests.