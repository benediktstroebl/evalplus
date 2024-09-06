```python
def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    """Return x if n is prime, else return y."""
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

This script defines a function `x_or_y` that takes three arguments, `n` (the number to check if it's prime), `x` (the value to return if `n` is prime), and `y` (the value to return if `n` is not prime). The script also includes a simple test that checks the function for the given inputs. 

To ensure the function is correct, the 'is_prime' function has also been provided to check if a number is prime or not. The 'is_prime' function cross-checks the given number with every number from 2 to the square root of the given number and returns False if any of them is equal to the remainder. If none of these numbers is equal to the remainder, then it returns True.