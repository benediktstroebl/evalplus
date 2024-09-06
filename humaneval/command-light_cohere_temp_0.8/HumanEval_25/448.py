```python
def factorize(n: int) -> List[int]:
    """Return list of prime factors of given integer in the order from smallest to largest"""
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    factors.append(n)
    return factors
```
This function uses the 'factorization' technique to get the prime factors of a given number. It uses a technique where it keeps dividing by prime factors (starting from 2, then 3, then 5, and so on) until the quotient becomes smaller than the target number. The function also handles cases where the number is even or odd, and finally, returns the list of prime factors in order from smallest to largest.