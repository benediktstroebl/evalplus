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