```python
def factorize(n: int) -> List[int]:
    """Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times corresponding to how many times it appears in factorization of the number.
    Input number should be equal to the product of all factors
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    for i in range(3, int(n**0.5) + 1,  :  # for square numbers
        factors.append(int(i**0))
        n = n // i

    if n > 2:
        factors.append(n)

    return factors
```