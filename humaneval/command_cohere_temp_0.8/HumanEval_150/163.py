```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    if is_prime(n):
        return x
    else:
        return y

# Tests
n = int(input("Enter a number: "))
print(x_or_y(n, 10, 6))
```

This code defines a function `x_or_y` that takes three arguments: an input number `n`, and two optional parameters `x` and `y`. The function will return `x` if the input number `n` is prime, and `y` if `n` is not prime, following the problem's description.

The code includes a test module, but you need to add your own tests as well. You can do so by assigning numbers to the `n` variable and using the `print` statement to see the output of the `x_or_y` function.