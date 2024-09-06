from typing import List
def factorize(n: int) -> List[int]:
    factors = []
    for i in range(2, n):
        if n % i == 0:
            count = 0
            while n % i == 0:
                n //= i
                count += 1
            if count > 0:
                factors.append(i)
                factors.extend([count] * count)
    if n > 1:
        factors.append(n)
        factors.extend([1] * (n - 1))
    return factors