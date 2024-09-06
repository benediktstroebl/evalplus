```python
def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        if x in row:
            result.append((i, row.index(x)))
    result.sort(key=lambda x: x[0])
    result.sort(key=lambda x: x[1], reverse=True)
    return result
```

The function iterates through each row in the list, checking each element to see if it matches the desired integer `x`. When a match is found, a tuple is created, consisting of the index of the row and the index of `x` within the row. This tuple is then added to the `result` list.

Before returning the list of tuples, the function sorts the tuples first based on the row index (`x[0]`), and then based on the column index (`x[1]`), but in descending order. This ensures that the coordinates are presented in the required order. 

The use of the `enumerate` function makes the code more concise, as it allows both the index of the row and the row itself to be accessed within the loop. Also, the `sort` method with a `key` parameter is used to sort the `result` list efficiently. 

This code ensures the correct output for the given problem statement and also ensures that the function is self-contained, not relying on any external variables or data that is not passed to the function.