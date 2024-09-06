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
    y = [ele for ele in x if not any(int(digit) % 2 == 0 for digit in str(ele))]
    return sorted(y)
```
This Python script solves the problem by taking a list of positive integers **x** as input. It uses a list comprehension to filter out elements that contain even digits. The function then returns a sorted list of these filtered elements, ensuring that the returned list is sorted in increasing order.

Here's an example usage of the function:
```python
>>> unique_digits([15, 33, 1422, 1])
[1, 15, 33]
>>> unique_digits([152, 323, 1422, 10])
[]
```
This example test demonstrates the function's behavior, returning the expected results based on the given input.