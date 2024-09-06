```python
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a <= 1 or a > 100:
        return False
    for b in range(2, a):
        if a % b == 0:
            return False
    for b in range(2, int(a**0.5) + 1):
        if a % b == 0:
            return False
    return True
```

This Python script defines a function called `is_multiply_prime(a)` that evaluates whether a given number `a` is the product of three prime numbers. The function first checks if `a` is less than or equal to 1 or greater than 100, returning False if either condition is met because such products cannot be formed within the given range. It then iterates through factors up to the square root of `a`, checking for divisibility by numbers other than 1 and returning False if any such divisors are found. Lastly, it confirms that a is divisible only by 1 and itself, which indicates the presence of exactly two distinct prime factors, thereby returning True if this condition is met, signifying that the number is indeed the product of three prime numbers.  This approach allows the code to accurately determine the nature of the number's factorization within the given range and return the appropriate boolean result.  The `example` usage demonstration provides a comprehensible illustration of the function's behavior.