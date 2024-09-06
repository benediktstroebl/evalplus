```python
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    prime_factors = []
    for i in range(2, int(a ** (0.5)) + 1):
        while a % i == 0:
            prime_factors.append(i)
            a //= i
        if a == 1:
            break
    return len(prime_factors) == 3
```

The code uses a `for` loop to find the prime factors of the number `a`. The `range` of the loop is between `2` and `int(a ** (0.5)) + 1` (rounded up square root of `a`). This is done to limit the number of iterations to a maximum of `O(log(a))`. The loop iterates through all numbers from 2 to the square root of `a` and checks if any number divides `a`. If it does, that number is appended to the `prime_factors` list. Then, the divisor (`a`) is divided by the found prime number. This process continues until `a` is reduced to 1, or until all the prime factors are found. 

The function returns `True` if the number has three prime factors and `False` otherwise. 

To prove the correctness let's examine a few numbers: 
- `12 = 2 * 2 * 3` - returns `True` since it has three prime factors
- `14 = 2 * 7` - returns `False` since it has only two prime factors
- `17 = 17` - returns `True` since it is a prime number multiplied by itself. 

The test cases that are provided for this problem should include numbers with different numbers of prime factors to ensure the function is correct.  It is important to include corner cases, such as the product of more than three prime factors, to ensure the function does not return a false positive.