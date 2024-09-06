```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers based on their index in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Sortedd list based on the criteria.
    """
    if len(nums) == 0:
        return []

    # Keep track of sorting order based on sum of digits and original index.
    sorted_order = []
    digit_sum_to_index = {}  # Dictionary for quick look-up of index based on digit sum.

    for index, num in enumerate(nums):
        digit_sum = sum(int(d) for d in str(num))
        sorted_order.append([digit_sum, index])
        digit_sum_to_index[digit_sum] = index

    # Sort the sorted_order list based on first element (sum of digits)
    sorted_order.sort(key=lambda x: x[0])

    # Generate the sorted result based on the sorted_order
    sorted_nums = [nums[idx] for idx in sorted_order[1]]

    return sorted_nums
```

This code snippet defines the `order_by_points` function, which takes a list of integers (`nums`) and sorts them according to the sum of their digits. If there's a tie, the tiebreaker is the index of the integer in the original list. The function is implemented using a nested list, where each element is a tuple containing the sum of digits and the index of the corresponding number. This nested list is then sorted primarily by the sum of digits and secondarily by the index. Finally, the function returns the sorted list of integers.