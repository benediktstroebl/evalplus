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

print(f'For x_or_y({n}, {x}, {y}) == {x_or_y(n, x, y)}')
```
This script defines a function `x_or_y` that takes three arguments `n` (which represents a number), `x` (return value for prime `n`), and `y` (return value for non-prime `n`). This function utilizes the `is_prime` function to check if `n` is a prime number. If `n` is prime, the function returns `x`; otherwise, it returns `y`. 

The `is_prime` function is also provided to check if a given number is prime. It employs a straightforward optimization of the sqrt(n) to speed up the testing for primality. The function returns True if the number is prime and False if not. 

The final lines are examples for the test cases to compare the outputs with the expected results. You can run this code to see the results and ensure that the function behaves as expected.  This code demonstrates a straightforward use of Python to solve the problem and implement the given function.