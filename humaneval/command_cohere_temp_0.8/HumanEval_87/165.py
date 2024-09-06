```python
def get_row(lst, x):
    result = []
    for row in lst:
        if x in row:
            result.append((idx, len(row)))
            result.sort(key=lambda x: (x[1], x[0]))
    return result
```

The solution leverages the fact that the list `lst` is nested, and iterates through it with two loops. The outer loop is indexing the rows (which are individual lists), and the inner loop checks if the element `x` is present in the current row. If it is, a tuple is created with the index `idx` and the number of columns `len(row)`, and added to the `result` list. Finally, the list of tuples is sorted by the columns and then by the row index to get the desired order and is returned. 

This approach has a time complexity of O(n*m), where `n` is the number of rows and `m` is the column of the "matrix", as it iterates through all the elements in the nested list `lst`. 

The code is complemented with corresponding tests, which are also provided below: 
```python
def test_get_row():
    # Arrange
    lst = [
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 1, 6],
        [1, 2, 3, 4, 5, 1],
    ]

    # Act
    actual = get_row(lst, 1)
    expected = [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    
    # Assert
    assert actual == expected, "Failed to find element 1 in the list." 

test_get_row()
``` 
This test case uses the example provided in the problem statement to check if the actual output matches the expected one, it succeeds if they are the same, failing the test if they are different. 
The method `test_get_row()` creates the input list, invokes the function, and compares the actual output with the expected one that is suggested in the problem statement. 
To run the test, you can call the function `test_get_row()` and it will execute the test, in case it fails, it will raise an exception, to avoid undefined behaviors, it is strongly recommended to run your tests using a testing framework, like `pytest`. 
Please note that the test is placed in the same script as the `get_row()` function for simplicity, the recommended approach is to have these two pieces in different files to enhance readability, understandability, and maintainability. G