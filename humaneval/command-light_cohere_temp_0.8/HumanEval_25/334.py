```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    for j in range(int(n**0.5) + 1, if n % (j+2) == 0 and j != 2:
        factors.append(j)
    return factors
```

This code defines a function called factorize, which takes an integer n as input and returns a list of prime factors of n in descending order. The function uses a divide the input n by 2 until it is even, and then checks for each prime factor individually. The function also handles the case where the input n is odd, and checks for prime factors that are congruitant with specific formula. 

Lastly, the function returns the list of prime factors.