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

For each index, the code checks if it's a multiple of 3 using the modulo operator `%`. If the index is a multiple of 3, the corresponding list element `num` is squared (`**= 2`) and added to the `result` variable. Similarly, if the index is a multiple of 4 but not a multiple of 3 (i.e., `i % 4 == 0` and `i % 3 != 0`), the corresponding list element `num` is cubed (`**= 3`) and added to the `result` variable.

If the index is not a multiple of 3 or 4, the list element `num` is left as is and added to the `result` variable.

Finally, the function returns the `result`, which represents the sum of all the modified list elements.

The code handles the edge cases outlined in the problem statement: if the input list is empty (`lst = []`), the function will return 0; if the list contains negative values, the sum will be negative, as demonstrated with `lst = [-1,-5,2,-1,-5]`, which returns `-126`.