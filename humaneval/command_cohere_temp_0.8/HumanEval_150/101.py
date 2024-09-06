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
print(f'x_or_y({n}, {x}, {y}) == {x_or_y(n, x, y)}') # Should print "34"

n = 15
x = 8
y = 5
print(f'x_or_y({n}, {x}, {y}) == {x_or_y(n, x, y)}') # Should print "5"
```

This script defines a function `x_or_y(n, x, y)` that takes three arguments, `n` (which is assumed to be either prime or non-prime), and two values `x` and `y` (which are replaced by the function with `n` if n is prime, and with non-prime `n`). The function implements the logic through an auxiliary function called `is_prime(n)` that checks if a number is prime or not. The program then conducts two tests that check the function's behavior for both cases (prime and non-prime). 

The program outputs the following:
```
34
5
```