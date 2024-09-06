```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1,):
        while n % i == 0:
            factors.append(i)
            n = n // i
    for num in range(int(n ** 0.5) + 2, )):
        if n % num == 0:
            factors.append(num)
    return factors
```
This script defines a function `factorize` that returns a list of prime factors of a given integer `n`. The function uses a `while` loop to repeatedly divide by 2 until the number is not divisible by 2. The function then uses another `while` loop to find all prime factors of the number by iterating through numbers from 3 to the square root of the number.