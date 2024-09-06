```python
def factorize(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) // i + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors
```
This function factorizes an input integer n by finding its prime factors and returns them as a list.

This function uses the "while" loop to find the prime factors of the number n. It checks for divisibility by incrementing integers from 2 up to the square root of the number. Then, it checks for each number in the list that evenly divides the number n, and if it does, it adds the number to the list of prime factors.