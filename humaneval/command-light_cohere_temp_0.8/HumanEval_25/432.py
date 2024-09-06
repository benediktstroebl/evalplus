```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1,  while n % i == 0:
        factors.append(i)
        n = n // i
    for i in range(int(n**0.5) + 2,  while n % (i*i) == 0 and i != factors[-1]:
        factors.append(i)
        n = n // i
    return factors
``` 
The function 'factorize' receives an integer 'n' as input and returns a list of prime factors of the given number. 

It works by first identifying the number's smallest prime factor and then iterates through larger prime factors until it finds all the prime factors. 

This approach ensures that the factors are listed in the order from smallest to largest, which is necessary for a correct factorization.