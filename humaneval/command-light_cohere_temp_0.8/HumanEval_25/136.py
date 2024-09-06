```python
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1,):
        while n % i == 0:
            factors.append(i)
            n //= i
    for j in factors:
        count = 0
        while n % j == 0:
            count += 1
        if count == factors[j]:
            factors.append(j)
    return factors
``` 
This Python function, `factorize()`, takes an integer `n` as input and returns a list of prime factors of the input number. The function first finds the prime factors using a `while` loop that iterates through the numbers from 2 to the square root of `n` and checks if `n` is divisible by each prime number using the modulo operator. 

Then, for each found prime factor, the function counts how many times it appears in the factorization and if this count is the same as the count of this prime factor in `n`, the function adds this prime factor to the list of factors. Finally, the function returns the list of factors.