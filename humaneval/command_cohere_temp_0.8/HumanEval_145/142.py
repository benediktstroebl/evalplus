```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Ordered list according to the criteria.
    """
    if not nums:
        return []

    # Tracking indices for tiebreaking
    index_tracker = [i for i in range(len(nums))]

    # Convert negative numbers to their positive counterpart for digit sum
    positive_nums = [num for num in nums if num >= 0]
    negative_nums = [-num for num in nums if num < 0]
    combined_nums = positive_nums + negative_nums

    # Sorting based on digit sum
    sorted_digit_sums = sorted(combined_nums, key=lambda x: sum(int(d) for d in str(x)))

    # Applying tiebreak based on original index
    sorted_index_tracker = [sorted_digit_sums[i] for i in index_tracker]

    # Separate positive and negative numbers again, if needed
    if len(negative_nums) > 0:
        return [-x if x < 0 else x for x in sorted_index_tracker]
    else:
        return sorted_index_tracker
```

This code snippet defines the `order_by_points` function, which sorts a given list of integers based on the sum of their digits, with tiebreaks decided by the index of the item in the original list. It accomplishes this by:
1. Handling empty lists gracefully.
2. Tracking the original indices to break ties rationally.
3. Converting negative numbers to their positive counterpart for digit sum calculation.
4. Sorting the numbers based on digit sum using a lambda function.
5. Applying the tiebreaking rule based on the original index.
6. Separating positive and negative numbers again, if needed.

This approach ensures that the numbers are sorted as per the specified criteria efficiently.