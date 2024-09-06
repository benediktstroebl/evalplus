from typing import List
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def factorize(n: int) -> List[int]:
    factors = []
    for i in range(2, n):
        if is_prime(i) and n % i == 0:
            factors.append(i)
            n //= i
            while n % i == 0:
                n //= i
    if n > 1:
        factors.append(n)
    return factors