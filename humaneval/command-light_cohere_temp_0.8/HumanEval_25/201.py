```python
def factorize(n):
    factors = []
    for i in range(1, int(n ** 0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    factors.append(n)
    return factors
```
This function, factorize, takes an integer n as input and returns a list of prime factors of n, ordered from smallest to largest, along with the count of each factor in the factorization.

The function uses a loop to iterate through the numbers from 1 to the square root of n, and checks if n is divisible by i. If it is, it adds i to the list of factors, and divides n by i.

The function then returns the list of factors, which are the numbers that divide n evenly. The function also returns the number of factors, which is the length of the list of factors.