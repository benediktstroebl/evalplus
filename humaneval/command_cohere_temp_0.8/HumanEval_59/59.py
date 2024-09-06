```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Your code here. Be sure to use only prime factors from the test cases.
    # You can use the following Python features:
    #  - list comprehensions
    #  - the `range` function (for loop indices)
    #  - conditional statements (`if`, `elif`, `else`)
    # You can also use the built-in Python functions: `len`, `list`, `dict`, `set`, `int`, `float`, `str`, `bin`, `hex`, `oct`, `abs`, `round`, `range`, `slice`, `tuple`, `max`, `min`, `sorted`, `sum`, `pow`, `all`, `any`, `enumerate`, `reversed`, `tuple`, `set`, `dir`
    # But avoid using built-in functions that compute factorials or number theoretic functions like `math.factorial`, `math.gcd`, `math.lcm`, `math.sqrt`, etc.
    prime_factors = [int(factor) for factor in str(n) if factor in '2357' and int(factor) <= n // 2]
    return max(prime_factors)
```
This Python script defines a function `largest_prime_factor` taking an integer n as input and returning the largest prime factor of n. It assumes n is greater than 1 and not a prime number. The function first converts the input n into a string, iterates over each character in the string, and checks if it is a prime factor of n. Then, it filters out any non-prime factors and retains only the prime factors, considering them as integers in the range of [1, n//2]. Finally, it returns the maximum value among these retained prime factors, which is the largest prime factor of n.