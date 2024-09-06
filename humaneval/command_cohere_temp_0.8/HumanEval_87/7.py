```python
def get_row(lst, x):
    result = []
    for row in lst:
        if x in row: 
            result.append((row.index(x), row.index(max(row)))) 
    return sorted(result, key=lambda x: x[0])
```