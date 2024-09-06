```python
def is_multiply_prime(a):
    # Write a function that returns true if the given number is the multiplication of 3 prime numbers
    # and false otherwise
    max_divisors = int(a ** (0.5)) + 1
    if max_divisors * max_divisors * max_divisors == a:
        return all(num == a for num in prime_factors(a))
    else:
        return False

def prime_factors(n):
    # TODO change to import sepmask
    import sepmask
    factors = sepmask.prime_factors(n)
    return factors
```

The function `is_multiply_prime(a)` aims to determine if the given number `a` is the product of three prime numbers. It first computes the prime factors of the given number `a` using the `prime_factors()` function (which uses the `sepmask.prime_factors()` function from the `sepmask` module). 

The `is_multiply_prime()` function then checks if the given number `a` has exactly three prime factors, by comparing the prime factors of `a` to `a` itself. If they are the same, then the number is a cube of a prime number and is therefore not a product of three distinct prime factors. Therefore, the function returns `True` in this case. Otherwise, the number is not a cube of a prime number, and the function returns `False`. 

The `max_divisors` variable is calculated as the square root of the given number `a` plus one. This is done to simplify the logic in checking if the given number `a` is indeed the product of three prime factors, as described above.

This code assumes the existence of a module called `sepmask` which has a function called `prime_factors()` that returns the prime factors of a given number. You may need to install the `sepmask` library with the following command: 
```bash
pip install sepmask
``` 

You should be aware that this code uses a library that is not commonly used in the Python ecosystem and may be prone to bugs or maintenance issues. It's recommended to use more established libraries, such as `math` or `numtel` for prime number factorization in Python.  If you prefer to not use the `sepmask` library, we can draft a version of the above function that uses another prime factorization library of your choice. 

If you would like to adapt this function for specific prime number factorization libraries, such as `math` or `numtel`, please specify which one, and I will provide an adapted version accordingly.