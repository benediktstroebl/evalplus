Here's a Python script with a self-contained function that solves the x_or_y problem and passes the tests provided in the prompt:
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
print(x_or_y(7, 34, 12))  # Output: 34
print(x_or_y(15, 8, 5))  # Output: 5
```

This script defines a function `x_or_y` that takes three arguments: an input number `n`, and two values `x` and `y` whose return is desired based on the primality of `n`. The function returns `x` if `n` is prime and `y` otherwise. 

The primality-checking function `is_prime` is also included, which checks whether a given number is prime or not. This function uses the deterministic primality testing algorithm called the `6k` rule. It checks if the given number is less than or equal to 3, then it is prime, or if the number is even or divisible by 3, then it is not prime. Finally, if the number is greater than 3, then the function checks if the number is divisible by any number in the interval [5, 8]. If no divisors are found, then the number is prime. 

The script then conducts two test cases for the `x_or_y` function, which correspond to the example cases provided in the problem statement, and prints the correct output for each one. 

This code is self-contained and can be run directly to demonstrate the behavior of the `x_or_y` function based on the primality of the input number `n`.  Let me know if it is helpful or if you have any concerns regarding the approach of the solution or any other additional details you would like to add!