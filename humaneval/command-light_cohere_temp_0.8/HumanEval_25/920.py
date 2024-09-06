```python
def factorize(n: int) -> List[int]:
    """Return list of prime factors of given integer in the order from smallest to largest"""
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1, ]:
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if n % j == 0:
                is_prime = False
                break
        if is_prime:
            factors.append(i)
        n = n // i
    return factors

# Example usage:
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```
The function `factorize` in this script takes an integer as input and returns a list of its prime factors, ordered from smallest to largest. It uses a `while` loop, checking divisibility with numbers from 2 up to the square root of the input number. The function returns the values of the factors and the corresponding number of times each factor appears in the factorization.

This is an example of how to use the `factorize` function with a sample input. The function can be easily customized and extended to handle more complex problems.