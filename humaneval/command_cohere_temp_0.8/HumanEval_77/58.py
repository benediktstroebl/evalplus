```python
def iscube(a):
    # Factorize the integer
    factors = []
    for i in range(2, int(a ** (1/3) + 1)):
        while a % i == 0:
            factors.append(i)
            a //= i
    if a != 1:
        factors.append(a)

    # Check if there are three equal factors
    return len(factors) == 3 and factors.count(factors[0]) == 3
```

This factorizes the number, checking for three equal factors, which would indicate a perfect cube. 

The code uses nested loops to iterate through potential factors, starting from 2 and stopping at the cube root of the number. It systematically divides the number by each potential factor, and the fact that the number is a perfect cube tells us that the resulting factors will have three identical factors. 

Thus, the length of the `factors` list will be three, and there will be three occurrences of the common factor, which the code verifies with the `count` method.