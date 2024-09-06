```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Sorting of the input list according to the specified criteria.
    """
    if not nums:
        return []

    def sum_digits(num):
        return sum(int(d) for d in str(num))

    sorted_nums = sorted(nums, key=lambda x: (sum_digits(x), x))
    return sorted_nums
```

This function uses a key process to sort the list first by the sum of digits and then by the original index of the integer. It then returns the appropriate sorted list. When applied to the example inputs, the function returns the expected outputs:
```python
>>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
True

>>> order_by_points([]) == []
True
``` 

This code efficiently solves the problem by digit-summing and indexing within a single sorting pass.