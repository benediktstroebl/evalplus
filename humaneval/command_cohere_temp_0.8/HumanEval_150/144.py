```python
def is_prime(n):
    """ Checks if a number is prime """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    """ Returns x if n is prime, else returns y """
    if is_prime(n):
        return x
    else:
        return y

# Tests
n = 7
x = 34
y = 12

print(f'x_or_y({n}, {x}, {y}) == {x}: {x_or_y(n, x, y) == x}')
print(f'x_or_y({n}, {x}, {y}) == {y}: {x_or_y(n, x, y) == y}')

n = 15
x = 8
y = 5

print(f'x_or_y({n}, {x}, {y}) == {x}: {x_or_y(n, x, y) == x}')
print(f'x_or_y({n}, {x}, {y}) == {y}: {x_or_y(n, x, y) == y}')
```
This code includes two functions. The first function, `is_prime`, determines whether or not a given number is a prime number. It verifies the eligibility criteria of the number being greater than one and examines whether the number is divisible by any integer between 2 and the square root of the number. If the number is not divisible by any such integer, it returns True, indicating that the number is prime; otherwise, it returns False.

The second function, `x_or_y`, uses the `is_prime` function to solve the problem. It takes three arguments: `n` (which is checked for primality), `x` (which should be returned if `n` is prime), and `y` (which should be returned if `n` is not prime). The function simply returns `x` if `n` is prime and `y` otherwise.

Finally, the code provides examples of using this x_or_y function with different inputs and prints the results to verify the function's correctness.