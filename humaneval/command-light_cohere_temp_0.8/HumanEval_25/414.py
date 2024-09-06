```python
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times which corresponds to how many times it appears in factorization of the given number.
    Input number should be equal to the product of all factors
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1,  while n % i == 0:
        factors.append(i)
        n = n // i
    for j in range(int(n ** 0.5) + 1,  while n % j == 0:
        factors.append(j)
    n = n // j
    for k in range(2 * int(n ** 0.5) + 1,  while n % k == 0:
        factors.append(k)
        n = n // k
    factors.append(int(n))  # added last prime factor

    return factors
``` 
Do you have any further questions about Python, coding, or other related concepts?