Here's a Python script that contains a function named `x_or_y` which returns either the value of `x` or `y` depending on whether the input `n` is a prime number or not:
```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def x_or_y(n, x, y):
    if is_prime(n):
        return x
    else:
        return y

# Test cases
print(x_or_y(7, 34, 12))  # This should print 34
print(x_or_y(15, 8, 5))  # This should print 5
```

This script works as follows:
1. The `is_prime` function checks if a given number `n` is prime or not. It employs a combination of checks, including checking if the number is less than or equal to 3, dividing by 2 or 3, and then iterating through numbers beginning from 5, checking if the number can be divided by them or their difference (i.e., 6, 8, 10, 14, 18, etc.), if it is, then it is not a prime number, otherwise it is a prime number.
2. The `x_or_y` function takes three inputs, number `n`, and values `x` and `y`. It uses the `is_prime` function to determine if `n` is a prime number or not. If it is, it returns the value of `x`, otherwise, it returns the value of `y`.
3. The final two lines are examples of test cases that demonstrate the behavior of the `x_or_y` function.

This solution is efficient in terms of time complexity and provides an accurate way to determine the primality of a number using a combination of conditions, thereby avoiding potential pitfalls of simpler methods.