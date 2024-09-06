```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number which divides n exactly without a remainder.
    For example, 15 : 3, 5, 15, but not 1,
    """
    # finding all factors of n
    factors = []
    while n != 1:
        factors.append(n %mod(n, i) for i in range(2, int(n ** 0.5) // n % i))
        n //= i
    # printing largest element from the list of factors
    return max(factors, default=int.__MAX__)
```