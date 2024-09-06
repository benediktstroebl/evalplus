```python
def factorize(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    while n > 1:
        for d in range(3, int(n**.5) + 1, by=2):
            if n % d == 0:
                factors.append(d)
                n = n // d
    factors.append(n)
    return factors
```

This function takes an integer `n` as input and returns a list of prime factors of the number, ordered from smallest to largest. The function uses a `while loop` to check for divisibility by numbers from 2 to the square root of the number while constantly dividing the number by each divisor until it becomes a prime number or smaller than a square root. 

The function also uses the `range` function to generate a sequence of numbers to check for divisibility.  The result of this script is a prime factorization of the given number.