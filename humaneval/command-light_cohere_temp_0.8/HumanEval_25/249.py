```python
def factorize(n: int) -> List[int]:
    factors = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    factors.append(n)
    return factors
```
This function, factorize, takes an integer n as input and returns a list of its prime factors in order from smallest to largest. It uses a algorithm of iterating through the numbers from 2 to the square root of n, and checking if n is divisible by each of these numbers. The function also returns the list containing n.