```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    if n < 2:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    for j in range(int(n**0.25),5 - 2):
        factors.append(j)
    n = n // j
    return factors

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

The function factorize returns a list of prime factors for a given integer n, ordered from the smallest to the largest. It uses a loop to find the prime factors, ensuring they are in the correct order.

This function, which can be reused to quickly get the prime factors of any number, is a good example of how functions can be self-contained and re-used in code.