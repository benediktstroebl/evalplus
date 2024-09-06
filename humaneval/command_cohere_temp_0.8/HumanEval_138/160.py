Here's a Python script that contains a function called `is_equal_to_sum_even` that solves the problem you've described:
```python
def is_equal_to_sum_even(n):
    even_nums = [2 * i for i in range(1, (n // 2) + 1)]
    return n == sum(even_nums)
```
This function generates a list of even numbers from 2 to n//2 and checks if the sum of these numbers is equal to n. The script should be self-contained and provide the functionality to evaluate the problem as described in the markdown code block.