```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Input:
        number = int(input('Enter a number: ')))
    if n <= 1:
        return []
    factors = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n = n // i
    factors.append(n)
    return factors
```
The function takes an input and returns a list of prime factors of the given number, it first checks if the number is less than or equal to 1, if it is, it returns an empty list, then it starts a loop from 2 to the square root of the number added by 1, while continuously dividing by the current factor until the number becomes 1, and saves the factor in the list of factors.