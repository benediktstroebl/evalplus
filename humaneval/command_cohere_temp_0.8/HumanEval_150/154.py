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

# Unit tests
tests = [
    (7, 34, 12, 34),
    (15, 8, 5, 5),
    (101, -10, 0, 0)
]

for n, x, y, expected in tests:
    actual = x_or_y(n, x, y)
    if actual != expected:
        print(f"For inputs {n}, {x} and {y}, expected {expected} but got {actual}")
        exit(1)

print('All tests passed')
```

The `is_prime` function is introduced to provide a more efficient primality test, and this script now includes unit tests to validate the `x_or_y` function. 

To see if the solution works, you can run this script. To see how the solution works, you can also look at the code.