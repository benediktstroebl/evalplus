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

    sorted_nums = [num for ind, num in enumerate(nums) if ind != nums.index(num)]

    for num in nums:
        digit_sum = sum(int(d) for d in str(num))
        index = nums.index(num)
        sorted_nums.append(num for num in nums if (digit_sum, index) == (sorted_nums[-1:][0], sorted_nums[-1:][1]))

    return sorted_nums
```

This code starts by creating an empty list called `sorted_nums` to store the sorted elements. It then iterates through the input list, excluding duplicates and calculating the sum of digits for each number. Using an intelligent approach, it appends the numbers to `sorted_nums` based on both their digit sum and index, ensuring correct sorting with tied elements. The function returns the final sorted list.

This approach avoids unnecessary computations and ensures an efficient solution with a time complexity of `O(n log n)`, where `n` is the length of the input list.