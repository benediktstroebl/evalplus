```python
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1,  while n % i == 0:
        factors.append(i)
        n = n // i
    factors.append(int)
    if n > 2:
        factors.append(n)
    return factors
```
This function, factorize, takes an integer n as input and returns a list of its prime factors in descending order. It utilizes a loop and checks for divisibility by successive numbers, starting from 3 up to the square root of n, until it reaches the square root. The function then checks if n is greater than 2 and adds the value of n to the list of factors if it is.