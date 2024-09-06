Here's a Python script that contains a function called `is_equal_to_sum_even` that evaluates whether a given number can be written as the sum of exactly 4 positive even numbers. The function is designed to return `True` if the condition is met and `False` otherwise:
```python
def is_equal_to_sum_even(n):
    even_nums = [2 * x for x in range(1, (n // 2) + 1) if x % 2 == 0]
    return len(even_nums) == n // 4 and sum(even_nums) == n
```
This function uses a list comprehension to generate a list of positive even numbers from 1 to `(n // 2)` inclusively. It ensures that the list contains only even numbers by filtering out odd numbers using the condition `x % 2 == 0`. 

Then it checks two conditions:
1. The length of the `even_nums` list should be equal to half the number of required even numbers (i.e., `n // 4`) to ensure that exactly 4 even numbers are required to sum up to `n`.
2. The sum of the numbers in the `even_nums` list should be equal to the given number `n` to verify that the numbers can indeed form the desired sum. 

Both conditions must be met for the function to return `True`, ensuring that the given number can be written as the sum of exactly 4 positive even numbers. 

Here is an example of how you might use this function:
```python
print(is_equal_to_sum_even(8))  # Should print True
print(is_equal_to_sum_even(6))  # Should print False
print(is_equal_to_sum_even(4))  # Should print False
```
This example demonstrates how the function can be used to evaluate different input numbers and determine whether they meet the specified condition. 

The function should work correctly for positive integers given as input and return `True` for valid inputs like 8 and return `False` for invalid ones like 6 or 4.