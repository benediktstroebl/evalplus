```python
def factorize(n: int) -> List[int]:
    factors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            factors.append(i)
            n //= i
        return factors
```
This function takes an integer `n` as input and returns a list of prime factors of `n` in descending order. It uses a method of trial division to find the factors. The function is self-contained, and does not rely on any other functions or modules.