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
    result = [i for i in x if not any(int(j) % 2 == 0 for j in str(i)]);
    return sorted(result)
```
This script uses a list comprehension that iterates over each element in the input list `x`, and verifies if the digit of every integer from the string representation of the element is divisible by `2`, utilizing the `any()` function. It then returns the list of integers that do not have any even digits. Finally, it returns a sorted list of those integers using the `sorted()` function.