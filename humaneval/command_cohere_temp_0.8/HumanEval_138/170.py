Here's a Python script that contains a function called `is_equal_to_sum_even` that solves the problem you've described:
```python
def is_equal_to_sum_even(n):
    even_nums = [2 * i for i in range(1, int(n**0.5) + 1)]
    return len(even_nums) == 4 and sum(even_nums) == n
```
This function iterates through natural numbers smaller than the square root of `n` and creates a list of all positive even numbers up to that square root. It then checks whether the list has exactly 4 elements and whether their sum equals `n`, as per the prompt's specifications.