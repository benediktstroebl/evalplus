```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    if is_prime(n):
        return x
    else:
        return y

# Tests
n = 7
x = 34
y = 12
print(f'x_or_y({n}, {x}, {y}) == {x_or_y(n, x, y)}') # Should print True

n = 15
x = 8
y = 5
print(f'x_or_y({n}, {x}, {y}) == {x_or_y(n, x, y)}') # Should print True
``` 

This script defines a function `x_or_y(n, x, y)` that takes three arguments, `n` (which is presumed to be either prime or non-prime), `x` (which will be returned if `n` is prime), and `y` (which will be returned if `n` is not prime). The prime-checking mechanism runs through a number's divisors from 2 up to the square root of the number, so it is quicker than checking all divisors from 1 to the number itself. It then uses the `is_prime` function to determine whether `n` is prime or not, and returns the corresponding value of `x` or `y`. The final part of the script serves as simple regression tests for this function against incorrect compositions of prime and non-prime numbers. 

Note that this version is somewhat optimized with a quicker algorithm for checking for primality, contrasted with a more elementary approach that might merely iterate from 1 to n and check for divisors. This allows the program to be more scalable and handle larger inputs more efficiently. 

Let me know if you would like me to explain any part of the code in more detail.