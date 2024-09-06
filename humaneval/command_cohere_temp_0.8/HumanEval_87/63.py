```python
def get_row(lst, x):
    res = []
    for i, row in enumerate(lst):
        cols = len(row)
        if cols == x:
            res.append((i, cols))
    res.sort(key = lambda x: (x[0], -x[1]))
    return res
```

The `get_row` function iterates through each row in the list, checking if the column count matches the target value `x`. If it does, a tuple of the format `(row_number, column_count)` is generated and appended to the `res` list. The list of tuples is then sorted first by the row number in ascending order and then by the column count in descending order using the `sort` method and a lambda function as the sorting key. The sorted list of tuples is returned as the output.

This approach ensures that the tuples are sorted first by the row number and then by the column count in descending order within each row. It efficiently finds the coordinates matching the given column count `x` and returns them in the desired format. 

The problem statement mentions a few test cases, but the provided code doesn't include the actual test cases to verify the functionality. If you want to test the code with specific input, you need to add a test case dictionary with input and expected output pairs, and then run the code with the `test_get_row` function. Here's an example:
```python
def test_get_row():
    # Test cases with input and expected output
    test_cases = {
        'example1': ([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 1, 6], [1, 2, 3, 4, 5, 1]], 1),
        'example2': ([[], [1], [1, 2, 3]], 3),
        'example3': ([[1, 2, 3, 4], [1, 2, 3, 4, 5], [1, 2, 3, 4, 6]], 4)
    }

    for case_name, test_case in test_cases.items():
        input_list, x = test_case
        expected = [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
        result = get_row(input_list, x)
        assert result == expected, f"For case {case_name}, expected {expected}, but got {result}"
``` 
Make sure to remove the preceding code block before executing the code, as it contains the actual implementation and test cases that conflict with each other.

The test cases in the `test_cases` dictionary are defined as tuples, with the first element representing the list of rows and the second element representing the target column count `x`. The expected output is provided as a list of tuples. The code executes each test case using the `get_row` function and verifies that the actual output matches the expected output.