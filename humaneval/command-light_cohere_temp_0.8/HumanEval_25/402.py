```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1,while n % i == 0:
        factors.append(i)
        n = n // i
    for num in range(int(n ** 0.5) + 1,while n % num == 0 and num != 1:
        factors.append(num)
    return factors
```

This function employs a loop and a list comprehension to determine and store the prime factors of the given integer. It starts with the loop, and the list comprehension, to identify the first two factors, which are 2 in this case. Then, it iterates through the loop, to identify the remaining prime factors, which are all numbers greater than 2 but less than the square root of n. Finally, it returns the list of prime factors in order, from smallest to largest.