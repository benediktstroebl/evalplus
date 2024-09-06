```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers decided by the index of the integer in the original list.

    Args:
        nums (List[int]): List of integers to be sorted.

    Returns:
        List[int]: Sorted list according to the specified criteria.
    """

    # Initialize a container to hold the sorted elements
    sorted_nums = []

    # Initialize a container to hold indices of elements with equal digit sums
    equal_sum_indices = {}

    # Iterate over the input list to compare and sort elements
    for idx, num in enumerate(nums):
        # Calculate the sum of digits of the current number
        digit_sum = sum(map(int, str(num)))

        # Store the index of elements with equal digit sums to break ties later
        if digit_sum not in equal_sum_indices:
            equal_sum_indices[digit_sum] = []
        equal_sum_indices[digit_sum].append(idx)

        # Append the element to the beginning of the sorted list
        sorted_nums.append(num)

    # Sort the indices of elements with equal digit sums
    for sum_ in equal_sum_indices:
        equal_sum_indices[sum_].sort()

    # Reconstruct the final sorted list while applying tiebreaker indices
    sorted_nums.sort()
    for sum_ in equal_sum_indices:
        for idx in equal_sum_indices[sum_]:
            sorted_nums.insert(idx, nums[idx])

    return sorted_nums
```

This code starts by initializing an empty list called `sorted_nums` to hold the elements after sorting. It then iterates through the input list, calculating the sum of digits for each integer and building a dictionary called `equal_sum_indices` to store the indices of elements with equal digit sums. After this, the elements are appended to the `sorted_nums` list in the order they will appear in the final sorted list, using the tiebreaker indices to restore the original order for elements with equal digit sums. The final step is to sort the list of indices for elements with equal sums and use them to insert the appropriate elements into `sorted_nums` in the correct order.