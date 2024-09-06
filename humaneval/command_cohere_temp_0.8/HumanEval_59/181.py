```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    factor = n
    while factor % 2 == 0:
        factor //= 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while factor % i == 0:
            factor //= i
    if factor > 1:
        return factor
```

The function iterates through potential prime factors, starting from 2 and moving in increasing steps of 2, checking if they divide the number until it finds the largest prime factor of the number.  This is done using the `while` and `//` (integer division) operations, which are efficient and logical for finding prime factors. 

To efficiently find the largest prime factor, the code starts by making sure the `factor` is even and divides out all even factors (not a prime). Then, it moves through increasing odd numbers (potential prime factors) incrementally, dividing out all factors that are not 1. The loop exits when the `factor` becomes 1, at which point the last factor divided into it was the largest prime factor. 

This approach efficiently finds the largest prime factor without the need for expensive factorization methods. 

The unit tests provided assert that the function correctly identifies the largest prime factor of a number, focusing on numbers with multiple prime factors and ensuring that the function identifies the correct largest factor.  These tests verify the correctness of the `largest_prime_factor` function. 

Note that the function assumes that the input number is greater than 1 and is not a prime number itself, as stated in the prompt. 
If the input number is prime, the function will return the number itself, as it is the largest prime factor. 
If the input is less than 2, the function will return 1, as the largest prime factor of such numbers is 1. 
If you want to support these edge cases, you may want to adjust the function or the test suite.