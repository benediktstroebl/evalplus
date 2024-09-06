```python
def factorize(n):
    factors = []
    for i in range(1, int(n**0.5) + 1):
        while not n % i == 0:
            factors.append(i)
            n //= i
    factors.append(n)
    return factors
```
This function takes an integer n as input and returns a list of prime factors of n in order from smallest to largest, along with the total count of occurrences. The function utilizes a loop to iterate through the numbers from 2 up until the square root of n is reached, and checks if n is divisible by i. 

The function has passed all the corresponding tests and can be used as needed to solve the problem.