from typing import List
def prime_factors(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors
def factorize(n: int) -> List[int]:
    product = 1
    factors = prime_factors(n)
    result = []
    for factor in factors:
        result.extend([factor] * (n // math.factorial(math.floor(n / factor))));
        product *= factor;
    assert product == n, f'Product ({product}) should be equal to the input number ({n}).'
    return result