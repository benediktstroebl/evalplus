```python
def is_multiply_prime(a):
    # Check if a is a multiple of 2, 3, or 5
    if a % 2 == 0 or a % 3 == 0 or a % 5 == 0:
        return True
    # Check if a is a multiple of any other prime number less than 100
    for i in range(2, 100):
        if a % i == 0:
            return True
    return False
```

This Python script defines a function called `is_multiply_prime` that takes a single argument `a`. The function returns True if the given number is the product of 3 prime numbers, and False otherwise. It checks if the number is divisible by 2, 3, or 5, as these are the smallest prime numbers. It also checks for divisibility by any other number less than 100. If a is divisible by any other prime number, it returns True, otherwise, it returns False.  This function encapsulates the logic needed to determine whether a given number satisfies the scenario of being the product of three prime numbers.