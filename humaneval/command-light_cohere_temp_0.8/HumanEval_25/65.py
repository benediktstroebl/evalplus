```python
def factorize(n):
    factors = []
    for i in range(1, int(n ** 0.5) + 1):
        is_prime = True
        while not is_prime:
            if n % i == 0:
                is_prime = False
            n //= i
    for i in range(1, int(n ** 0.5) + 1):
        if i > factor[i - 1]:
        factors.append(i)
    return factors
```
This function takes an integer n as input and returns a list of its prime factors in descending order. The function uses a iterative approach to find the prime factors of the number.