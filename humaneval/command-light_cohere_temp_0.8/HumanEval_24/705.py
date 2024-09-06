```python
def largest_divisor(n: int) -> int:
    """ Returns the largest integer that divides n exactly """
    if n <= 1:
        return n
    # prime factorization of n
    pf = prime_factors(n)
    # largest divisor from pf
    ldiv = max(pf, default = 1)
    # return the largest divisor
    return ldiv

def prime_factors(n: int) -> List[int]:
    """ Returns the prime factors of the number n """
    if n <= 1:
        return []
    if n <= 3:
        return [1]
    if n % 2 == 0:
        return [2] + prime_factors(n // 2)
    for i in range(3, int(n**0.5),n):
        + [i]*(n // i) == n
    while n % i == 0:
        n //= i
    return [i for i in range(3, int(n**0.5),n)]

# test cases
print(largest_divisor(15)) # 5
print(largest_divisor(17))# 17
```