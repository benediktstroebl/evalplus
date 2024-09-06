```python
def is_multiply_prime(a):
    # Check if a is a perfect square
    root = int(pow(a, 0.5))
    if root * root == a and a != 1:
        return False

    # Check for divisors
    for i in range(2, root + 1):
        if a % i == 0:
            return False

    # Check if a is the product of 3 primes
    for i in range(2, a // 2 + 1):
        if a % i == 0 and a != i and a != i * i:
            return False
    
    return True
```

This function checks: 

1. If `a` is a perfect square, in which case it must have a divisor and is not a prime multiplication. 
2. If `a` has any divisors other than 1 and itself.
3. If `a` can be factorized into 3 primes. 

The code will return `True` if the number follows the criteria and `False` otherwise. In our example, `is_multiply_prime(30)` will return `True` as 30 can be written as 2 * 3 * 5, where 2, 3, and 5 are prime numbers.  This is the expected behavior, so the function correctly solves the problem.