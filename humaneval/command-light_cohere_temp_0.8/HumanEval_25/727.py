```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    for i in range(int(n**0.5) + 2, while n % i == 0:
        factors.append(i)
        n = n // i
    return factors
``` 
This function uses the Sieve of Eratosthenes to find prime factors of the given number. It works by iterating through the square of the number, and if the square is divisible by any prime number starting from 3, then the corresponding prime number is added to the list of prime factors.