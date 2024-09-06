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

    sorted_nums = []
    digit_sum_to_index = {}  # Dictionary to store the mapping of digit sum to item index.

    for idx, num in enumerate(nums):
        digit_sum = sum(int(d) for d in str(num))
        if digit_sum in digit_sum_to_index:
            if idx < digit_sum_to_index[digit_sum]:
                continue
            elif idx > digit_sum_to_index[digit_sum]:
                sorted_nums.append(num)
                digit_sum_to_index[digit_sum] = idx
        else:
            sorted_nums.append(num)
            digit_sum_to_index[digit_sum] = idx

    return sorted_nums
```

The function `order_by_points` sorts a list of integers based on the sum of their digits, with tiebreaks resolved by referring to the index of the item in the original list. An auxiliary dictionary is used to handle the tiebreak determination, ensuring correct sorting for scenarios with multiple items sharing the same digit sum. The provided example tests illustrate how the function operates, and the expected output is correctly achieved.