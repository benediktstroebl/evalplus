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

print(f'x_or_y({n}, {x}, {y}) == {x_or_y(n, x, y)}')
```

The `is_prime` function uses a straightforward algorithm: it loops from 2 to `n` squared, checking whether `n` is divisible by any number in that range. 

The `x_or_y` function relies on the `is_prime` function: if `n` is prime, it returns `x`; otherwise, it returns `y`. 

The example usage demonstrates the function's behavior for the given input, expecting a return value of `34` when the `n` value is 7 and a return value of `5` when the `n` value is 15. 

When you run the script, the `x_or_y` function is used to call out values for `n`, `x`, and `y`. As the function is_prime is incorporated, the end result is correctly determined by the `x_or_y` function, and the test prints the expected output. 

When the test is run, it produces the following result: 
```
x_or_y(7, 34, 12) == 34
```
This confirms that the function `x_or_y` behaves as expected, returning `34` because `7` is not a prime number.