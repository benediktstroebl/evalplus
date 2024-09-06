Here's a Python script with a self-contained function that solves the problem and passes the tests:
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

# Example usage
print(x_or_y(7, 34, 12))  # Output: 34
print(x_or_y(15, 8, 5))  # Output: 5
```

This code defines a function `x_or_y` that takes three arguments: an input number `n`, and two values `x` and `y` whose return is dependent on the input number `n`. The function utilizes the `is_prime` function to determine if `n` is a prime number or not. If `n` is prime, the function returns `x`, else it returns `y`.

The `is_prime` function is also included, which checks if a given number is prime or not. It employs a straightforward optimization by checking only up to the square root of the number, excluding the need to check higher integers. 

The code could be optimized further by incorporating a faster primality testing algorithm like the 'Sieve of Eratosthenes' for more exceptional efficiency, particularly with larger numbers. Nonetheless, the provided code achieves the basic goal and fulfills the requirements of the prompt.