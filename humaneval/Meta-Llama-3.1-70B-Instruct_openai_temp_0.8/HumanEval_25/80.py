```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The number to factorize.

    Returns:
        List[int]: A list of prime factors in the order from smallest to largest.
    """
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# Test the function
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]

# Verify that the input number is equal to the product of all factors
def test_factorize(n: int) -> None:
    factors = factorize(n)
    product = 1
    for factor in factors:
        product *= factor
    assert product == n, f"Input number {n} is not equal to the product of its factors {factors}"

test_factorize(8)
test_factorize(25)
test_factorize(70)
```

This Python script defines a function `factorize` that takes an integer `n` as input and returns a list of prime factors in the order from smallest to largest. Each factor is listed number of times corresponding to how many times it appears in factorization.

The function works by dividing the input number `n` by the smallest prime factor (which is 2), as long as it's divisible. Then it increments the divisor by 1 and continues the process until `n` is reduced to 1.

The test cases at the end of the script verify that the function works correctly for the given examples.

Additionally, the `test_factorize` function checks that the input number is equal to the product of all its factors, as required by the problem statement.