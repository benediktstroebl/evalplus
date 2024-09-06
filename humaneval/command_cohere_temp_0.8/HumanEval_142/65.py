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

The code uses a for loop to iterate through each index and corresponding value in the input list `lst`. The conditionals `i % 3 == 0` and `i % 4 == 0 and i % 3 != 0` ensure that the squares and cubes operations, respectively, are only applied to list elements with indexes that are multiples of 3 and 4, respectively. Finally, the sum of the modified values is returned as the result.