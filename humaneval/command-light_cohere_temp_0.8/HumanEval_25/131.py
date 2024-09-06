```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5)+1,  while n % i == 0:
        factors.append(i)
        n = n // i
    for j in range(int(n**0.25),3), string.digits(j):
        n = n // (j*j)
    factors.append(int(j))
    return factors
```
The function factorize in the above code takes an integer n as input and returns a list of prime factors of the number n, in order from smallest to largest. The function first checks if n is less than or equal to 1, and if so, returns an empty list. If n is greater than 1, it iterates through the numbers from 2 to the square root of n, checking if n is divisible by each number. The function then appends each divisible number to the list of factors. The function then returns the list of prime factors of the given number n.