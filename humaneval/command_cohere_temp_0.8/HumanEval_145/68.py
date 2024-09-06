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

    # Iterate through the list and calculate the digit-wise sum for each integer
    digit_sums = [sum(int(d) for d in str(num)) for num in nums]

    # Sort the integers based on the sum of their digits in ascending order
    sorted_nums = sorted(nums, key=lambda num: (digit_sums[nums.index(num)], nums.index(num)))

    return sorted_nums
```

This code begins by checking if the input list is empty; if so, it returns an empty list. It then proceeds to calculate the digit-wise sum for each integer in the list using a list comprehension. Next, it sorts the list of integers based on the sum of their digits in ascending order, using a lambda function as the sorting key. The lambda function prioritizes sorting based on the digit sum, and as a tiebreaker, it sorts based on the index of the integer in the original list. Ultimately, the function returns the sorted list.