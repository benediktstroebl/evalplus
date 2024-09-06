```python
def choose_num(x, y):
    max_even = max((z for z in range(x, y + 1) if z % 2 == 0), default=-1)
    return max_even
```

The code uses a generator expression with a range and a filter based on the modulo check of even numbers to find the biggest even number in the range `[x, y]` and uses `default=-1` in the max function to handle the edge case where no such number exists in the range. 

To handle the edge case where no even number is found in the range, the default value of `-1` is returned instead of throwing an error or returning an invalid value. 

You can test this function by calling it with different arguments to check if it returns the expected values based on the problem statement.