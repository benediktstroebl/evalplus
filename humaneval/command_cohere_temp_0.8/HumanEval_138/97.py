```python
def is_equal_to_sum_even(n):
    # Check whether the given number can be expressed as the sum of 4 positive even numbers
    # First, check if the number is less than 4
    if n < 4:
        return False
    # Number greater than 4, check if it's divisible by 2
    elif n % 2 == 0:
        return True
    else:
        return False
```

This function checks whether the given number n can be expressed as the sum of exactly four positive even numbers. It returns True if it can be expressed this way, and False otherwise. It checks if the number is less than 4 first, as a number smaller than 4 cannot be expressed as a sum of four even numbers. If the number is greater than 4, it checks if the number is even. If it is, it returns True, as an even number greater than 4 can be expressed as a sum of four even numbers (e.g., 8 = 4 + 4). If the number is odd, it returns False, as an odd number greater than 4 cannot be expressed as the sum of exactly four even numbers.