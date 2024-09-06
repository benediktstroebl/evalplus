```python
def get_row(lst, x):
    result = []
    rows = []
    for idx, row in enumerate(lst):
        if x in row:
            result.append((idx, len(row)))
            rows.append(row)
    result.sort(key=lambda x: (x[0], -x[1]))
    rows = sorted(rows, key=lambda x: x.index(x))
    return [(-row[0], row) for row in rows for x in range(len(row) + 1)]
```

The solution utilizes two nested lists, `result` and `rows`, to store the result and rows of the list, respectively. The outer loop iterates through each row in the list, checking each element for the value `x`. When a match is found, a tuple is generated and added to the `result` list. Additionally, the current row is appended to the `rows` list. Both the `result` and `rows` lists are then sorted accordingly. The final output is a list of tuples, where each tuple represents a coordinate (row, column) of the value `x` found in the list. The nested list `rows` is used to generate the columns for each row, ensuring the correct columns are associated with the correct rows. The overall time complexity of this approach is O(n log n), where n is the number of rows in the list.