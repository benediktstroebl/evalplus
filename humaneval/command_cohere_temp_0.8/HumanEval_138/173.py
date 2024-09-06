Here's a Python script that contains a function called `is_equal_to_sum_even` that solves the problem you've described:
```python
def is_equal_to_sum_even(n):
    """
    Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    :param n: Number to be evaluated
    :return: True if it can, False otherwise
    """
    if n <= 0:
        return False

    # Try to write n as sum of 4 even numbers
    for i in range(1, int(n**0.5) + 1):
        if n == i * 4:
            return True
        if n == (i * 2) + (i * 2) + (i * 2) + (i * 2):
            return True

    return False

# Unit tests
def test_is_equal_to_sum_even():
    assert is_equal_to_sum_even(8) == True
```
This script defines the `is_equal_to_sum_even` function, which takes a number `n` as input and returns either `True` or `False` depending on whether `n` can be written as the sum of exactly 4 positive even numbers. It also includes a basic unit test to validate the function's behavior for the given input. 

The function first checks if `n` is less than or equal to 0, in which case it returns `False` since no positive even numbers can sum up to 0 or be equal to negative numbers. Then it iterates through numbers from 1 to the square root of `n` incrementing by 2, and checks if the number can be expressed as a sum of 4 even numbers.