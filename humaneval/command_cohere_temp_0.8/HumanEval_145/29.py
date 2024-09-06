```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums:
        return []

    # Calculate the sum-of-digits score for each number
    digit_sums = [sum(int(d) for d in str(n)) for n in nums]

    # Split the list into tiers based on digit sum
    tier_groups = [nums[idx:next_idx] for idx, next_idx in enumerate(
        range(0, len(digit_sums), 1))
                    if digit_sums[idx:] == digit_sums[idx:next_idx]]

    # Sort each tier separately with the tiebreaker being the index
    sorted_nums = [tier for tier in tier_groups if tier]
    for i in range(len(sorted_nums)):
        tier = sorted_nums[i]
        # If there's a tie, sort by the index of the first element
        tier.sort(key=lambda x: (x, tier.index(x)))

    return sorted_nums[0] if sorted_nums else []
```

This code begins by checking if the input list is empty; if so, it returns an empty list. It then calculates the digit sum for each number using a list comprehension and distributes the numbers into tiers based on their digit sums using the `enumerate` function.

It sorts each tier of numbers using the `sort` method with a custom key function that sorts first by the value with the tiebreaker being the index of the number in the original list. Finally, it returns the sorted list, or an empty list if the original was empty.

Note that this code is specifically designed to return a list of integers, as per the prompt. If the input list contains other data types, those items will not be included in the output.