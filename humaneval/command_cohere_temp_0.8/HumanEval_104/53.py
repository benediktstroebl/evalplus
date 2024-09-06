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
    strangest = [ele for ele in x if not any(int(digit) % 2 == 0 for digit in str(ele))]
    return sorted(strangest)
```
This Python script solves the problem by taking a list of positive integers **x** as input. It utilizes a list comprehension to filter out elements that contain even digits. The function creates a list of those elements that do not contain any even digits, indicated by `strangest`. Then it sorts this list in increasing order and returns the resulting sorted list.

The `unique_digits` function works correctly for the given test cases, as depicted in the below example:
```python
# Test case for unique_digits
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
```