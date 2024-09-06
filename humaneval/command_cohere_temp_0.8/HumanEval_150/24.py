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
    """ Returns x if n is prime, otherwise returns y """
    if is_prime(n):
        return x
    else:
        return y

# Tests
n = 7
x = 34
y = 12

print(f'x_or_y({n}, {x}, {y}) == {x}')
assert x_or_y(n, x, y) == x

n = 15
x = 8
y = 5

print(f'x_or_y({n}, {x}, {y}) == {y}')
assert x_or_y(n, x, y) == y
```
This script defines a function `is_prime` that checks if a number is prime and a function `x_or_y` that returns the value of `x` if the given number is prime, and `y` otherwise. It then tests the function with two examples as provided. 
The `is_prime` function first returns `False` if the number is less than or equal to one. It then iterates through the numbers from 2 to the square root of the number and returns `False` if the number is divisible by any of them. If it is not, it returns `True`.  This is a basic check for primality but is not optimized for large numbers. 

The `x_or_y` function simply calls `is_prime` and returns either `x` or `y` based on the result. 

The tests confirm that the script behaves as expected for the given inputs. 

It's worth noting that the `is_prime` function can be optimized for better performance, especially for larger numbers. There are more efficient algorithms, such as the Sieve of Eratosthenes, that are particularly useful for checking multiples of relatively small primes.