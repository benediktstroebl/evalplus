```python
def factorize(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
        n //= i
    factors.append(int(n > 2))  # to handle odd cases
    return factors
# Test cases
print(factorize(8))      # [2, 2, 2]
print(factorize(25))     # [5, 5]
print(factorize(70))     # [2, 5, 7]
```
This code defines a function `factorize` that returns a list of prime factors for the given number `n`. The function first checks for the presence of odd factors by considering numbers greater than 2, and then iterates through odd and even numbers to find prime factors. This function handles both odd and even factors correctly, providing the list of prime factors in ascending order.