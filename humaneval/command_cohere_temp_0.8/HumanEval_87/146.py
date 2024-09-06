```python
def get_row(lst, x):
    result = []
    for row in lst:
        row_x = [col for col in row if col == x]
        if row_x: 
            result.append((idx, len(row_x)))
            result.sort(key=lambda x: (x[0], -x[1]))
    return result
```

The solution leverages the fact that Python collections have a defined __len__ method, so the length of a given row can be determined via list(row). Moreover, the list comprehension allows for element filtering and retrieval, whereas the sorting is handled effortlessly by the built-in sorting key lambda function. Ultimately, this results in a concise and efficient solution.