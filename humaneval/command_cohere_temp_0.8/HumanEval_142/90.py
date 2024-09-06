```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            num = num ** 2
        if i % 4 == 0 and i % 3 != 0:
            num = num ** 3
        result += num
    return result
```

The code uses a for loop to iterate through each index `i` and corresponding value `num` in the input list `lst`. The desired operations are computed within the loop and the result is returned at the end. The function is self-contained and does not require any external dependencies to work.