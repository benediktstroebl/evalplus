```python
from typing import List
def factorize(n: int) -> List[int]:
    """Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are returned number of times which corresponds to how many times it appears in factorization of the number.
    :param n: int
        :return: List[int]
    """
    if n <= 1:
        return []
    factors = []
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            factors.append(i)
            while n /= i
    factors.append(int(n))  # Added last element which is always the largest prime factor
    return factors
def test_factorize() -> None:
    try:
        n = 25
        factors = factorize(n)
        assert len(factors) == 5
        print(factors)
    except Exception as e:
        print("An error occurred:", str(e))
```