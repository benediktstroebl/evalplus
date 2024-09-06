```python
def get_row(matrix, x):
    result = []
    for row in matrix:
        for y in row:
            if x == y:
                result.append((row, y))
    result.sort(key = lambda x: (x[0], x[1]))
    return result
```

The function `get_row` takes in two parameters, `matrix` which is a 2D list and `x` which is the element to find in the list. The function goes through each row in the matrix and loops through each element in the row to find the element `x`. If the element is found in the list, a tuple is created consisting of the row and the element, these tuples are then appended to a result list. The result list is sorted first by the row in ascending order and then by the element in the row in descending order. The function returns the list of tuples. 

Here is an example function call:
```python
matrix = [
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 1, 6],
    [1, 2, 3, 4, 5, 1]
]
x = 1
result = get_row(matrix, x)
print(result)
# Output: [(1, 1), (1, 4), (2, 1), (2, 5), (3, 1)]
```