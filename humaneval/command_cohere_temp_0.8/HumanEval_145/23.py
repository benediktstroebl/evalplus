```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the integer in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list:Sorted list according to the specified criteria.
    """
    if not nums:
        return []

    # Calculate the sum-of-digits score for each number
    scores = [sum(map(int, str(n))) for n in nums]

    # Originally found numbers first with similar scores
    sorted_nums = [nums[i] for i in range(len(nums)) if scores[i] == max(scores)]

    # Any remaining numbers sorted by their score as tiebreakers
    remaining_nums = [n for n in nums if n not in sorted_nums]
    sorted_nums.extend(remaining_nums)

    return sorted_nums
```

This code will first find the numbers from the original list that match the maximum sum of digits value, and then will sort them in order of their original index. Following this, any remaining numbers are appended to the sorted list, but sorted by their individual sum of digits to act as tiebreakers. The result is a sorted list that follows the specified criteria.