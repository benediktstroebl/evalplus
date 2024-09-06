```python
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1, ]:
        while n % i == 0:
            factors.append(i)
            n = n // i
    factors.append(n)
    return factors
```
This function takes an integer n as input and returns a list of prime factors of n in descending order. It uses a list comprehension and a while loop to find all the prime factors of n. The time complexity of this function is O(sqrt(n)), as it uses the same factorization technique as the previous function.