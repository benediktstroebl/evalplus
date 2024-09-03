```python
def is_multiply_prime(a):
    """
    Function to check if a is the multiplication of 3 prime numbers
    :param a: integer to check, must be less than 100
    :return: boolean
    """
    # uses sieve of Eratosthen
    is_prime = [True] * (a//2)
    is_prime[0] = False # 0 is not prime
    is_prime[1] = False # 1 is not prime
    for p in range(2, int(a**0.5):
        if is_prime[p]:
            for i in range(p*p, a, p*p):
                is_prime[i] = False
    return a % (2 * 3 * 5) == 0
```