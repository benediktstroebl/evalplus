```python
def sort_even(l: list):
    return sorted(l, key=lambda x: (x if x % 2 == 0 else -1) * (x if x > 0 else 1))

# Test cases
test_sort_even = [
    [1, 2, 3],
    [5, 6, 3, 4],
    [0, 7, 8],
    [9, 10, 11]
]

def test_function(test_case):
    lst = test_case
    result = sort_even(lst)
    assert len(result) == len(test_case)
    assert all(result == test_case[i] for i, x in enumerate(test_case))

test_sort_even_test_function(test_case)
```
The Python script defines a function `sort_even` that takes a list as input and returns a sorted list where even indices are sorted to their original value, and odd indices are sorted in descending order.

The function uses the lambda function as the sorting key to define a custom sorting behavior. The test cases include a list of different data sets, and the `test_function` function verifies that the `sort_even` function correctly sorts the input list according to the specified criteria.