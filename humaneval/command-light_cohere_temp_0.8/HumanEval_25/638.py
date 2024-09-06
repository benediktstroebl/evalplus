```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times corresponding to how many times it appears in factorization
    Input number should be a positive integer
    """
    if n <= 1:
        return []

    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1,):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors
```
This Python function, `factorize`, takes a single parameter `n`, which represents the number for which the prime factors are being found. The function follows the basic algorithm for finding prime factors:
1. First, the function checks if `n` is less than or equal to 1, in which case it returns an empty list.
2. If `n` is greater than 1, it proceeds to the next step.
3. The function then appends the 2 to the `factors` list. This is because 2 is the only even prime factor, and it appears first in the factorization.
4. Then, the function enters a for all the factors that can be divided by 2, starting from 3 and moving up to the square root of n.
5. Finally, if there is still a factor greater than 2, it is also added to the `factors` list.
6. The function then returns the list of prime factors of the given number `n`, ordered from smallest to largest.

In summary, the function efficiently finds and returns the prime factors of a given positive integer.