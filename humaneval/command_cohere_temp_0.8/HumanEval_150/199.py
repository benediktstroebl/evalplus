```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def x_or_y(n, x, y):
    if is_prime(n):
        return x
    else:
        return y

# Unit tests
tests = [
    (7, 34, 12, 34),
    (15, 8, 5, 5),
    (101, -5, 7, 7),
    (0, 10, 11, 11),
    (4, 2, 3, 3),
    (16, 23, 2, 2),
    (107, 34, 43, 43)
]

for n, x, y, expected in tests:
    assert x_or_y(n, x, y) == expected
```

This script defines a function `x_or_y` that takes three arguments (`n`, `x`, and `y`) and returns `x` if the integer `n` is prime and `y` if n is not prime. The function calls the `is_prime` function to determine whether `n` is prime. The script also includes a list of tests that verify the function's behavior. 

The `is_prime` function checks whether a given number n is prime or not. It returns `True` if the number is prime and `False` otherwise. The function uses a mix of small prime numbers and composites to test n. It starts by checking if n is less than or equal to 3, as these are the smallest primes. It then checks if n is divisible by 2 or 3, as these are some of the most common primes and composites. If not, it begins iterating through potential divisors of n starting from i = 5. It checks for divisors at intervals of 6 (i.e., 5, 11, 17, 23, 29, ...) to cover both even and odd divisors. It ensures that n is not divisible by any of these potential divisors. If it reaches a point where the loop doesn't find any divisors, it returns True, indicating that n is a prime number; otherwise, it returns False, indicating that n is composite. 

The `x_or_y` function uses the `is_prime` function to solve the original problem. It takes three arguments: `n` (an integer), `x` (a value to return if `n` is prime), and `y` (a value to return if `n` is not prime). The function checks if the `is_prime` function returns `True` for `n` and returns `x` if it does; otherwise, it returns `y`. 

Finally, the script's test suite consists of multiple test cases with different values for `n`, `x`, `y`, and expected outputs to ensure the `x_or_y` function behaves as expected. Each test case verifies that the function returns the expected value corresponding to each input. 

 
You can copy and paste this code into a Python environment or script to test it out. Feel free to modify the test cases to your liking to evaluate different prime and composite numbers.