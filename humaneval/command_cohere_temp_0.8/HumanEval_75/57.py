```python
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100 and a > 1:
        for i in range(2, round(sqrt(a)) + 1):
            if a % i == 0:
                if i == (a//i):
                    return False
                else:
                    j = a//i
                    while j != i and j != 1:
                        if j == (a//j) and j != i:
                            return False
                        j = j//2
                    if j == 1:
                        return True
                return False
        return True
    return False
```

The algorithm works by dividing the number a by each number from 2 to the square root of `a` and checking if any of them is a divisor of a but not a duplicate of it. If so, the number is not a multiplication of three primes. If not, it proceeds to divide each potential divisor by 2 until it reaches the largest potential divisor is 1. If so, it returns true, and if not, it returns false.