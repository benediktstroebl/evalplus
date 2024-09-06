```python
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be the number of times it appears in the factorization
    :param n: given integer
    :return: list of integers
    """
    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)
   
    for i in range(3, int(n**.5) + 1, 2):
        if n % i == 0:
            factors.append(i)
            n /= i
    factors.append(n)
    return factors
```
This function employs the 'division by power rule' to repeatedly divide by the smallest prime factor (2) until the number becomes prime. The function then appends the smallest prime factor(s) found during the division. The function is designed to run in O(log n) time complexity, which is quite efficient for most practical applications.