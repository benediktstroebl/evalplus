```python
def is_multiply_prime(a):
    # check if a is divisible by 2 or 3
    if a % 2 == 0 or a % 3 == 0:
        return False

    # check if a is divisible by any number in range 5 to the square root of a
    for i in range(5, int(a**0.5) + 1, 2):
        if a % i == 0:
            return False

    return True
```

This function checks if the number `a` is divisible by 2 or 3, then checks if `a` is divisible by any number in the range 5 to the square root of `a`. If a is divisible by any number in this range, it returns False, otherwise, it returns True.