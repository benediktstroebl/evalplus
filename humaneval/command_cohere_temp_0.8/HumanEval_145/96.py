```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list:Sorted list according to the specified criteria.
    """
    if not nums:
        return []

    sorted_nums = [num for ind, num in enumerate(nums) if ind == num]
    sorted_nums.sort(key=lambda x: sum(map(int, str(x))), reverse=False)

    return sorted_nums
```

This code snippet defines the `order_by_points` function, which sorts a list of integers based on the sum of their digits, with ties broken by their index in the original list. The function first creates a list `sorted_nums` of elements that match their index in the input list. Then, it sorts this list based on the sum of the digits of each element, in ascending order. The `enumerate` function is used to track the original index of each number during the sorting process. The code efficiently handles both empty inputs and lists with varying sizes and content.