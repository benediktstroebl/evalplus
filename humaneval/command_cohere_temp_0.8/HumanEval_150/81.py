Here's a Python script with a self-contained function that solves the x_or_y problem and passes the tests provided in the markdown code block:
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

# Example usage
print(x_or_y(7, 34, 12))  # Output: 34
print(x_or_y(15, 8, 5))  # Output: 5
```

This script defines a function `x_or_y` that takes three arguments: an input number `n`, and two values `x` and `y` whose return is dependent on the input number `n`. The function uses the `is_prime` function to determine whether `n` is a prime number or not. If it is prime, the function returns `x`, else it returns `y`.

The `is_prime` function also defines a simple algorithm to determine whether a number is prime or not. It checks whether the number is less than or equal to 3, in which case it is prime. It also checks whether the number is divisible by 2 or 3, in which case it is not prime. The function then starts checking for divisors from 5 onwards, incrementing by 6 each time to narrow down the possible divisors. 

The example usage demonstrates the expected behavior of the `x_or_y` function for the provided test cases.