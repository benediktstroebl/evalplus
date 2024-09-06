```python
def get_row(lst, x):
    result = []
    for row in lst:
        cols = len(row)
        if x == cols:
            result.append((len(lst) - row.index(True), cols))
    result.sort(key=lambda x: (x[0], -x[1]))
    return result
```

The solution works by using a nested loop that traverses the list `lst` and identifies the rows that contain the integer `x`. The row indices are appended to the result list as the first element, whereas the column count is appended as the second element, in a tuples. The resulting list of tuples is then sorted first by row index in ascending order and then by column count in descending order using the `sort` method and a lambda function as the sorting key. 

The tests are not included in this solution, but they can be added to validate the functionality of the code. 
Here is an example of how tests could be incorporated:
```python
def test_get_row():
    # [] and 0 case
    assert get_row([], 0) == []

    # Edge case
    assert get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]

    # Multiple occurrences of element
    assert get_row([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

    # Non-existing element
    assert get_row([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 100) == []
```