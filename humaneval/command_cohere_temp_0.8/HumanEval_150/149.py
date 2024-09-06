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
    """ Returns x if n is a prime number, otherwise returns y """
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
This script utilizes a straightforward algorithm to check if a number is prime or not. Consequently, it returns the 'x' value if the number is prime, and the 'y' value if it is not. This is demonstrated through explicit tests that ensure the correctness of the `x_or_y` function. 

Note that the `is_prime` function has a small flaw, as it doesn't consider numbers <= 1 to be prime, and returns false in those cases.