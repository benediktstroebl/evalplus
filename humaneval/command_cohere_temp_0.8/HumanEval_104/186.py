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
    y = [ele for ele in x if not any(int(d) % 2 == 0 for d in str(ele)]);
    return sorted(y)
```
This script employs a list comprehension to examine each element in the input list `x` and determine whether any of its digits are even. It does so by iterating through each digit in the string representation of the element and checking whether any digit, when interpreted as an integer, is divisible by two. 

The `any()` function combines these individual checks into a single boolean value indicating whether any odd digit exists in the element. Finally, the element is included in the `y` list if no even digit is found.

The function finally returns a sorted version of `y`, ensuring the output is appropriately sorted in ascending order. 

This approach ensures the correctness of the problem statement in terms of finding elements lacking even digits and sorting them as required.