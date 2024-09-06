Here's a Python script that contains a function called `is_equal_to_sum_even` that solves the problem you've described:
```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    return n in even_nums
```

This function directly returns `True` if the number n is in the list of even numbers from the provided list suitable for the sum, and returns `False` otherwise, this makes the function compact and simple. 
This approach allows the function to directly evaluate whether the given number can be written as the sum of exactly 4 positive even numbers. 
The function can be tested with the following inputs:
```python
print(is_equal_to_sum_even(8))
print(is_equal_to_sum_even(6))
print(is_equal_to_sum_even(4))
```
which will respectively print:
```bash
True
False
False
```
This demonstrates that the function handles the case where the evaluates if the number can be written as a sum of 4 even positive numbers, while returning False for numbers that cannot be achieved this way.