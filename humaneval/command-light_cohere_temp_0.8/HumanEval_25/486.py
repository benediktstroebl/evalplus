```python
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5), i += 2):
        if n % i == 0:
            factors.append(i)
            n = n // i
    for i in range(int(n**0.5) + 1, i += 2):
        if n % i == 0:
            factors.append(i)
            n = n // i
    return factors

# Tests
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```