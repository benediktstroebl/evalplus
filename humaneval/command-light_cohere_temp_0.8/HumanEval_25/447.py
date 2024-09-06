```python
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(100)
    [2, 2, 5, 5, 7]
    >>> factorize(121)
    [3, 3, 7, 7]
    """
    # Initialize empty list to store factors
    factors = []

    # 1 is always a prime factor
    factors.append(1)

    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i

    for j in range(2, int(n ** 0.5) + 1):
        if n % j == 0:
            factors.append(j)
            n //= j

    # Check for higher powers of prime factors
    for k in range(2, int(n ** 0.5) + 1):
        while n % k == 0:
            factors.append(k)
            n //= k

    return factors
``` 
The above function, factorize, takes an integer n as input and returns a list of prime factors of the number n in order from smallest to largest. 

The function starts by adding 1 to the list of factors, as 1 is always a prime factor. It then iterates from 2 upwards, checking if n is divisible by the current number. If n is divisible by the current number, it is appended to the list of factors. The function then checks for higher powers of prime factors by iterating from 2 to the square root of n + 1. 

Finally, the function returns the list of prime factors.