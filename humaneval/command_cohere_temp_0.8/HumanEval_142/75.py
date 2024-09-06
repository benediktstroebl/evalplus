```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            result += num ** 2
        elif i % 4 == 0 and i % 3 != 0:
            result += num ** 3
    return result
```

The function operates on a list of integers, squares any integer at an index that is a multiple of 3, and cubes any integer at an index that is a multiple of 4 but not 3, while leaving other numbers unchanged. The final sum of the modified numbers is then returned. The `enumerate()` function is used for convenient indexing and numeral iteration, and a `result` variable is used to track the sum of the modified numbers.