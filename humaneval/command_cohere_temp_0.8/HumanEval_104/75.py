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
    result = [ele for ele in x if not any(int(digit) % 2 == 0 for digit in str(ele))]
    return sorted(result)
```
This Python script solves the problem by taking a list of positive integers `x` as input. It uses a list comprehension to filter out elements that have at least one even digit, which is achieved by checking if any digit in the string representation of the element is even (using the `int(digit) % 2 == 0` condition). The resulting list of elements meeting the criteria is then sorted in increasing order using the `sorted()` function and returned as the answer.

To follow the specification of the problem, the code includes the clarifying note in the function docstring and provides example queries in the function signature. These clearly explain the expected behavior of the function and its input/output.

This code provides a self-contained solution to the problem in a well-documented manner. You can easily execute it directly in the Python environment or import it into your Python project.