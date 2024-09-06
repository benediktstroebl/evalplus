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

The code uses a for loop to iterate through each index and entry in the input list `lst`. The `enumerate` function is used to access the index `i` and the value `num` of the list element simultaneously.

For each index, the code checks if it's a multiple of 3 using the modulo operator `%`. If the index is a multiple of 3, the corresponding list element `num` is squared (`**= 2`) and added to the result. If the index is a multiple of 4 but not a multiple of 3 (i.e., `i % 4 == 0` and `i % 3 != 0`), then the list element `num` is cubed (`**= 3`) and added to the result.

If the index is not a multiple of 3 or 4, then the list element `num` is left as is, and it's added to the result as is. Finally, the function returns the calculated result.

This code solves the problem using a single, self-contained `sum_squares` function as requested.