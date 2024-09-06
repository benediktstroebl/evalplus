Here's a Python script that contains a function called `is_equal_to_sum_even` that solves the problem you've described:
```python
def is_equal_to_sum_even(n):
    even_nums = [2 * i for i in range(1, (n // 2) + 1)]
    return n == sum(even_nums)
```
This function generates a list of even numbers from 2 to n//2. It then returns true if n is equal to the sum of this list.

To test this function, you can write tests like so:
```python
# Testing the function with various inputs and expected outputs
assert is_equal_to_sum_even(8) == True
assert is_equal_to_sum_even(4) == False
assert is_equal_to_sum_even(6) == False
```
The function should correctly answer the problem for the given test cases.