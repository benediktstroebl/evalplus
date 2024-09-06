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
    y = [ele for ele in x if not any(int(dig) % 2 == 0 for dig in str(ele)]))
    return sorted(y)
```
This script defines a function `unique_digits` that takes in a list of positive integers `x` and returns a sorted list of elements that do not contain any even digits. It uses a list comprehension to filter out the elements that contain any even digits, and the returned list is sorted in increasing order.

Here's an example of how you can use the function with the given test cases:
```python
# Test case for a list with one element not containing even digits
test_list = [15, 33, 1422, 1]
test_case_result = unique_digits(test_list)
print(test_case_result)  # Output: [1, 15, 33]

# Test case for a list with no elements not containing even digits
test_list = [152, 323, 1422, 10]
test_case_result = unique_digits(test_list)
print(test_case_result)  # Output: []
```

This would give the following outputs:
```
[1, 15, 33]
[]
```

Note that the function uses the `any()` function with a generator expression to efficiently check for any even digits in the elements of the list.