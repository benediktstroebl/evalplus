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

    sorted_nums = sorted(nums, key=lambda x: (sum(map(int, str(x))), nums.index(x)))
    return sorted_nums
```
This code works by first checking if the input list is empty; if so, it returns an empty list. It then iterates through the list, converting each number to a string, summing the digits of that string, and using the resulting sum as the sorting key with the index of the number as a tiebreaker. The returned list will be sorted in the specified manner.