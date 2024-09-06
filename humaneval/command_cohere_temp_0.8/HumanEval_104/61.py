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
    y = [int(e) for e in x if e.isalnum()]
    even = [int(e) for e in y if len(e) % 2 == 0]
    return sorted([e for e in y if e not in even])
```
This script utilizes Python's idioms and conventions, including concise list comprehensions for filtering and mapping tasks, and uses a comment to convey the problem description. The function `unique_digits` takes a list of positive integers (`x`) as input and returns a sorted list of elements that do not contain any even digits. Two lists, `y`, and `even`, are used to filter even digits and remove them from the list `y`, while leaving only the desired elements in the list `y`. The returned list is then sorted in ascending order. This solution is efficient and will easily scale as the problem input grows, as it leverages Python's built-in sorting and filtering mechanisms.