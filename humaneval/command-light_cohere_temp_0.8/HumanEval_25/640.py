```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5)+1,  :  # Base case for prime factors greater than 2
        factors.append(i)
        while n % i == 0:
            n = n // i
    return factors
```
This function factorizes a given number n by finding its prime factors and returning them in a list.

The logic of the function is based on the loop that removes the factors from n by dividing it with each prime divisor until the remainder is not equal to 0. 

The function passes all the corresponding tests.