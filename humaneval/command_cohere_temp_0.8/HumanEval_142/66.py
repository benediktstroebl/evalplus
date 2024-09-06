```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            num **= 2
        elif i % 4 == 0 and i % 3 != 0:
            num **= 3
        result += num
    return result
```

The code uses a for loop to iterate through each index and corresponding value in the input list `lst`. The conditionals `i % 3 == 0` and `i % 4 == 0 and i % 3 != 0` ensure that the right operation is applied to each number, and the result is correctly updated accordingly.