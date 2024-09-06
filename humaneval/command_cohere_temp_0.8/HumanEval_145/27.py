```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    Args:
        nums (list): List of integers

    Returns:
        list: Ordered list based on criteria above
    """
    if not nums:
        return []

    def sum_of_digits(num):
        return sum(map(int, str(num)))

    sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), nums.index(x)))
    return sorted_nums
```

This code defines the `order_by_points` function, which sorts a list of integers according to the sum of their digits. If there is a tie, the tie is broken by using the index of the number in the original list. It first checks if the input list is empty, returning an empty list if so. It then sorts the numbers using a custom key function that calculates the sum of digits and the original index, leveraging the `sorted` function. The resulting sorted list meets the criteria set forth in the problem statement.