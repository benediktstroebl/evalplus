```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Ordered list based on the criteria.
    """
    if len(nums) == 0:
        return []
    summed_digits = []
    for num in nums:
        sum_ = 0
        for digit in str(num):
            sum_ += int(digit)
        summed_digits.append(sum_)
    sorted_nums = sorted(nums, key=lambda x: (summed_digits.index(sum_), x))
    return sorted_nums
```

This code starts by checking if the input list is empty; if so, it returns an empty list. Otherwise, it creates a new list called `summed_digits`, where each element is the sum of the digits of a corresponding number in the input list. It then sorts this list using a lambda function as the key, which first finds the index of the sum in the `summed_digits` list (the tiebreaker) and then returns the original number. Finally, the function returns the sorted list.