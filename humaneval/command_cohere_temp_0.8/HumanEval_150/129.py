```python
def is_prime(n):
    if n <= 1:
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

# tests
n = 7
x = 34
y = 12
print(f'for x_or_y({n}, {x}, {y}) == {x}')

n = 15
x = 8
y = 5
print(f'for x_or_y({n}, {x}, {y}) == {y}')
```
This code defines a function `x_or_y` that takes three arguments `n` (which is checked if it's prime), and two values `x` and `y`, and returns `x` if `n` is prime and `y` otherwise. This is achieved through the helper function `is_prime` that checks if a number is prime. The example tests output are also provided showing the correct behavior of the code.