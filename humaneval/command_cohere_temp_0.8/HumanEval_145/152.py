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

    summed_digits = []
    original_indices = [i for i, n in enumerate(nums)]

    for n in nums:
        summed = sum(map(int, str(n)))
        summed_digits.append(summed)

    sorted_nums = sorted(zip(summed_digits, original_indices), key=lambda x: x[0], reverse=False)
    return [n for idx, n in sorted_nums]
```

The function `order_by_points` sorts a list of integers based on the sum of their digits, with tiebreaks resolved by using the original index of the item. It accomplishes this in two main steps:
1. A list called `summed_digits` is created to store the sum of digits for each number, and another list called `original_indices` is created to store the original indices of each number in the input list.
2. The list `sorted_nums` is created by zipping the lists `summed_digits` and `original_indices`, sorting them based on the first element (the summed digit score), and then returning the sorted numbers with their original indices.

The resulting list `sorted_nums` is then returned as the final sorted list of numbers, with the numbers sorted in ascending order first by their digit sum and then by their original index in case of ties.