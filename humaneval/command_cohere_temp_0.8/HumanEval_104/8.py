```python
def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    result = [i for i in x if not any(int(j) % 2 == 0 for j in str(i)]))
    return sorted(result)
```

This script provides a function `unique_digits` that takes in a list of positive integers `x` and returns a sorted list of elements in the list that contains no even digits. The function uses a list comprehension that iterates over each element in the input list, checking if any digit in the string representation of the element is even. If no even digits are found, the element is added to the result list. The final result is sorted in increasing order.

The unit test is provided as follows:
```python
def test_unique_digits():
    # Test case 1
    input1 = [15, 33, 1422, 1]
    expected1 = [1, 15, 33]
    assert unique_digits(input1) == expected1

    # Test case 2
    input2 = [152, 323, 1422, 10]
    expected2 = []
    assert unique_digits(input2) == expected2

test_unique_digits()
```

This provides a test case that checks the function against the two provided examples in the statement of the problem.