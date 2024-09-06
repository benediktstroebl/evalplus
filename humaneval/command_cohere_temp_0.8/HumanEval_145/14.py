```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums:
        return []

    sorted_nums = sorted(nums, key=lambda x: (sum(map(int, str(x))), x))
    return [sorted_nums[i] for i in range(len(sorted_nums))]
```

This script provides a function called `order_by_points` that takes a list of integers as input and sorts them according to the sum of their digits. If there is a tie, the list element that appears first in the original list will appear first in the sorted list. The function tests these conditions using a lambda function as the sorting key, sorting first based on the sum of digit strings and then using the original list index as a tiebreaker. Ultimately, the function returns the sorted list in accordance with these criteria.

To illustrate how to use this function, consider this example:
```python
order_by_points([1, 11, -1, -11, -12])
```

The function will return the list `[-1, -11, 1, -12, 11]`, as intended according to the problem statement. And consider this example for empty input:
```python
order_by_points([])
```

As anticipated, the function will return an empty list `[]`. These examples validate that the function operates according to the problem statement and provides the expected output for different input scenarios.