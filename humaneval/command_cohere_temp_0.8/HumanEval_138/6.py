Here's a Python script that contains a function called `is_equal_to_sum_even` that solves the problem you've described:
```python
def is_equal_to_sum_even(n):
    """
    Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    """
    if n < 0:
        return False
    elif n % 2 == 1:
        return False
    else:
        half_n = n // 2
        return half_n % 2 == 0
```

This function first handles edge cases where n is negative or odd. For odd numbers, it returns False since the sum of positive even numbers will always be odd, hence cannot be represented as the given number. For negative numbers, it also returns False as there cannot be a sum of positive even numbers equal to a negative number. For cases where n is even, it checks if n // 2 is also even to ensure it can be represented as the sum of 4 positive even numbers.

To test this function, you can write an if statement that uses the `is_equal_to_sum_even` function and prints out the appropriate output format, similar to the examples you provided:
```python
if is_equal_to_sum_even(4):
    print("False")
elif is_equal_to_sum_even(6):
    print("False")
elif is_equal_to_sum_even(8):
    print("True")
```

This would provide an accurate assessment of the function's behavior for the provided examples.