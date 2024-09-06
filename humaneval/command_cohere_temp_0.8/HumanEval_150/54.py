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
n = int(input("Enter a number: "))
print(x_or_y(n, 10, 6))
```

This script defines a function `x_or_y` that takes three arguments (`n`, `x`, and `y`) and returns `x` if `n` is prime and `y` if `n` is not prime. 

The `is_prime` function is utilized to determine if a number is prime. It employs a straightforward algorithm that verifies if the number is less than 2 or if it has any divisors between 2 and the square root of the number. If there are no divisors, the number is prime.

To exemplify the function, the code includes a test case where the user is prompted to input a number, and the `x_or_y` function is applied to this number, with the results displayed thereafter.