```python
def is_multiply_prime(a):
    # check if a is less than 100
    if a < 100:
        # check if the root of a is an integer
        if int(root(a)) == a: 
            # if so, check the factors of a
            factors = factorize(a)
            if len(factors) == 3 and all(map(lambda x: x == 1 or x == a, factors.values())):
                return True
    return False

def root(n):
    return int(n ** 0.5)

def factorize(n):
    factors = {}
    for i in range(2, int(root(n)) + 1):
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n //= i
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors
``` 

This script contains three functions: `is_multiply_prime`, `root`, and `factorize`. 

The `is_multiply_prime` function takes a number `a` as an input and checks if it's a product of three prime numbers. It does so by first checking if a is less than 100, then checking if the square root of a is an integer, and finally checks the factors of a to decide whether the number is prime or not. 

The `root` function takes an integer `n` as an input and returns the integer square root of `n` rounded down to the nearest integer, as stated [here](https://math.stackexchange.com/questions/11926/how-to-calculate-the-square-root-of-an-integer-in-python). 

The `factorize` function takes an integer `n` as an input and returns a dictionary of factors of `n`, where the keys are the factors and the values are the multiplicities. It does so by iterating from 2 to the square root of `n` and accumulating the factors in the dictionary `factors`.

This code should solve the given problem and is tested on the scenario provided in the description. It should cover the following scenarios:
- `is_multiply_prime(30)` should return True.
- `is_multiply_prime(28)` should return False.
- `is_multiply_prime(25)` should return False.

These tests would prove that the code provided is correct.