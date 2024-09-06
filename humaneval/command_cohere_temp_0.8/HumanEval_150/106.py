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

# tests
n = 7
x = 34
y = 12

print(f'for x_or_y({n}, {x}, {y}) == {x}')
assert x_or_y(n, x, y) == x

n = 15
x = 8
y = 5

print(f'for x_or_y({n}, {x}, {y}) == {y}')
assert x_or_y(n, x, y) == y
```

In the above code, the `is_prime` function checks if a number is prime or not. It employs the tried-and-tested strategy of checking if the number is divisible by any number between 2 and the square root of the number. The `x_or_y` function accepts the number, along with the values to return for prime and non-prime inputs, respectively, and returns accordingly. The final part of the code tests the function on the given examples from the prompt and asserts the expected results. 

If you are interested in more advanced or nuanced approaches to primality testing, you may consider looking into the `millions_test` or `fermat` tests, which are more efficient but slower and more complicated to implement, respectively. 

Let me know if I can provide further refinement or additional test scenarios to ensure robustness of the solution.