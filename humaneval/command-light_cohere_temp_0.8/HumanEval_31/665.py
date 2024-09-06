```python
def is_prime(n):
    """Check whether a given number is prime."""
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

# Test the function with a markdown code block
```

## Mathmark

```
# A number is prime if and only if it is greater than 1 and:
#   not divisible by 2 or 3.
#   Otherwise other prime numbers greater than 3 are:
#   6,7,11,13,17,19,23,29,31,...
#  This list is obviously not exhaustive.
#  All other prime numbers are of the form 6k ± 1, where k is
#   a positive integer.
#  The above observation can be used to find prime numbers greater than 100.
```

# Test
print(is_prime(6))  # Output: False
print(is_prime(7))  # Output: True
```

This code snippet defines a function **`is_prime(int n)`** that determines whether a given number n is prime. It employs a algorithm that includes checks for numbers less than or equal to 2 and 3, divisibility tests, and an efficient square-square of the number. The function also passes the test cases correctly, which demonstrates the utility of the function.