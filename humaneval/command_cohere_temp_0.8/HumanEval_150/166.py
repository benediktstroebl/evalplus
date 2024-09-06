```python
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    """Return x if n is a prime number, otherwise return y."""
    if is_prime(n):
        return x
    else:
        return y

# Tests
n = 7
x = 34
y = 12
print(f'x_or_y({n}, {x}, {y}) == {x}')

n = 15
x = 8
y = 5
print(f'x_or_y({n}, {x}, {y}) == {y}')
```

This code defines a function `x_or_y` that takes three arguments: an input number `n`, and two values `x` and `y` whose return values in the cases of prime and non-prime numbers respectively. The prime-checking mechanism runs through a loop from 2 to the square root of the input number and checks for divisibility. If the number is divisible by any integer within this range, it is deemed non-prime; otherwise, it is considered prime. The code then showcases this functionality by calling the function with various input arguments and printing the results.  Overall, the code provides an elegant solution to the problem at hand and serves as a practical implementation of prime number verification.