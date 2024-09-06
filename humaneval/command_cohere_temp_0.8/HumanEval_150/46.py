Here's a Python script with a self-contained function that solves the problem and passes the tests:
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

This script defines a function `x_or_y` that takes three arguments: an input number `n`, and two values `x` and `y` whose return is dependent on the input number `n`. The function utilizes the `is_prime` function to check if the number `n` is prime. If `n` is prime, the function returns `x`, else it returns `y`. 

The `is_prime` function also checks if a number is less than or equal to 3, as these numbers are by default prime. It also checks if a number is divisible by 2 or 3, and if so, it returns `False`. The `i` variable cycles through numbers 3, 7, 13, 19, and so on, to optimize the primality check. 

Lastly, the script provides examples that show the working of the `x_or_y` function. 

Note: this implementation has a time complexity of O(sqrt(n)) for the `is_prime` function, meaning it can efficiently determine primality for larger numbers compared to simpler methods.