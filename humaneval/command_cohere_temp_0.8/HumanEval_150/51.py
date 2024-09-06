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
n = 7
x = 34
y = 12

print(f'x_or_y({n}, {x}, {y}) == {x_or_y(n, x, y)}')
assert x_or_y(n, x, y) == x

n = 15
x = 8
y = 5

print(f'x_or_y({n}, {x}, {y}) == {x_or_y(n, x, y)}')
assert x_or_y(n, x, y) == y
```

In the above code, the `is_prime` function is used to efficiently check if a number is prime or not. If the number is prime, the `x_or_y` function returns the value of `x`; otherwise, it returns the value of `y`. The code also includes basic tests that verify the function against sample inputs. 

Let's break down the code:
- The `is_prime` function takes a number `n` as an argument and checks if it is prime or not. 
- It first checks if `n` is less than 2, returning `False` if so.
- Then, it iterates through the numbers from 2 to the square root of `n` (inclusive), and for each number `i`, it checks if `n` is divisible by `i`, returning `False` if it is. 
- If no divisors are found, it returns `True`, indicating that the number is prime.
- The `x_or_y` function takes three arguments: `n` (the number to check), `x` (to return if `n` is prime), and `y` (to return if `n` is not prime).
- It calls the `is_prime` function to determine if `n` is prime. 
- If `n` is prime, the function returns the value of `x`. Otherwise, it returns the value of `y`.
- The final two lines provide example calls to the `x_or_y` function, and the outputs are printed and then checked with `assert` statements to ensure they are correct. 

This code combines these two functions to solve the problem efficiently and adheres to the problem statement provided.