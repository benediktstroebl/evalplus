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

The code uses a for loop to iterate through each index and value in the input list `lst`. The `enumerate` function is used to access the index `i` and the value `num` of the list element.

If the index of the element is a multiple of 3, the value of the element is squared and the squared value is added to the `result` variable. If the index of the element is a multiple of 4 but not a multiple of 3, the value of the element is cubed and the cubed value is added to the `result` variable.

The function leaves the list elements untouched if their index is not a multiple of 3 or 4. Finally, the function returns the `result`, which is the sum of the modified values. 

This code solves the problem using a for loop to iterate through the list and apply the necessary transformations. The conditions within the for loop check for the index modulo to 3 and 4 to determine whether to square or cube the elements. The result is then returned as the sum of the modified values.