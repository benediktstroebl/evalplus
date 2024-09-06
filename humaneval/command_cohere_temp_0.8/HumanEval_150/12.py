```python
def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    """Return x if n is prime, else return y."""
    if is_prime(n):
        return x
    else:
        return y

# Test cases
print(x_or_y(7, 34, 12))  # Output: 34
print(x_or_y(15, 8, 5))  # Output: 5
```

This code defines a function `x_or_y` that takes three arguments: an input number `n`, and two values `x` and `y` whose values should be switched depending on the primality of `n`. The code employs a straightforward algorithm to verify whether a number is prime or not. The 'is_prime' function iterates through numbers from 2 to the square root of the input number `n` and checks if `n` is divisible by any of them. If `n` is not divisible by any of these numbers, it is considered prime.

The `x_or_y` function then utilizes the `is_prime` function to ascertain whether `n` is a prime number. If it is, the function returns `x`; otherwise, it returns `y`.

The final part of the code provides test cases to confirm the functionality of the program, printing out the output of the `x_or_y` function with various input arguments. The outputs are also commented so that you can easily verify the correctness of the function.