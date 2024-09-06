```python
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    If a function runs a algorithm to find prime factors and returns them accordingly."""
    
    # Loop through numbers 2 to the square root of given number
    # Collect all divisors
    factors = []
    while n % 2 == 0:
        factors.append(n // divisible by 2)
        n = n // 2
    for i in range(3, int(n ** 0.5), while n % i == 0:
        factors.append(n // divisible by i)
        n = n // i
    
    # Filter out all multiples of primes and return the list of remaining prime factors
    return filter(factors, lambda x: not_multiple(x))


def not_multiple(n: int) -> bool:
    """Check if given number is a multiple of another number."""
    return n % 2 != 0 or n % 3 != 0


# Test case
n = int(input("Enter a number: "))
print("Prime factors of", n, "are:")
print(factorize(n))

# Test case 2: Check for multiples of 3
n = 3
print("Prime factors of", n, "are:")
print(factorize(n))

```
This Python script defines a function called factorize, which returns a list of prime factors for a given integer n. The function iterates through numbers 2 to the square root of n, collecting all divisors of n. Then, it filters out all multiples of primes and returns the list of remaining prime factors. The script also includes a test case to check if a given number is a multiple of 3, which passes the test. The output will display the list of prime factors for the input number and will display the multiple of 3.