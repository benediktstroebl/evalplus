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
    if len(nums) == 0:
        return []

    summed_digits = [sum(map(int, str(num))) for num in nums]
    indexed_nums = list(zip(nums, summed_digits))
    
    sorted_nums = sorted(indexed_nums, key=lambda x: (x[1], x[0]))
    return [num for num, _ in sorted_nums]
```

This code provides a function called `order_by_points` that takes a list of integers as input and sorts them according to the sum of their digits. If there's a tie, the element that originally appeared first in the list will appear first in the sorted list. The sorting is performed in the following steps:
1. An intermediate list `summed_digits` is created, where each element is the sum of the digits of a corresponding element in `nums`.
2. Another intermediate list `indexed_nums` is created, where each element is a tuple of the original integer and its corresponding sum of digits.
3. The list `indexed_nums` is sorted in ascending order based on the second element (the sum of digits), and in the event of a tie, the first element (the original integer) acts as a tie-breaker.
4. Finally, the original list `nums` is reconstructed by unpacking the sorted `indexed_nums` list into a list of integers only.