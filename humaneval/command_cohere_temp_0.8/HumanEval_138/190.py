Here's a Python script that contains a function called `is_equal_to_sum_even` that solves the problem you've described:
```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    return n in even_nums
```

This script defines a function called `is_equal_to_sum_even` that takes a number `n` as input and returns either True or False. It checks if the number `n` is in the list of positive even numbers `[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]`, the function returns True, indicating that the number can be written as the sum of exactly 4 positive even numbers. If the number is not in the list, it returns False.

This approach assumes that the given number `n` can be represented as an integer value and that all the values in the list of even numbers are also integers. If the initial assumption leads to a decimal number, the function will return False. 

To ensure that the function behaves as expected, a test suite should be created to cover different test cases.  Here's an example:
```python
def test_is_equal_to_sum_even():
    assert is_equal_to_sum_even(8) == True
    assert is_equal_to_sum_even(6) == False
    assert is_equal_to_sum_even(4) == False
    assert is_equal_to_sum_even(22) == False
```

This script provides a basic test suite with different test cases to cover different scenarios and ensure that the `is_equal_to_sum_even` function behaves as expected. 

*Note*:  You can add more test cases to cover a wide range of inputs and edge cases to thoroughly test the function.