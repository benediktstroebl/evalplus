```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers decided by the index of the digit in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums:
        return []

    # initialize the list to store sorted numbers and the dictionary to store digit sums
    sorted_nums = []
    digit_sum = {}

    # calculate the digit sums of all numbers and store in the dictionary
    for num in nums:
        dig_sum = 0
        numstr = str(num)
        for digit in numstr:
            dig_sum += int(digit)
        digit_sum[num] = dig_sum

    # sort the digit sums in ascending order, using the index as a tiebreaker
    sorted_keys = sorted(digit_sum.keys(), key=lambda x: (digit_sum[x], nums.index(x)))

    # rebuild the sorted list from the sorted keys
    for key in sorted_keys:
        sorted_nums.append(key)

    return sorted_nums
```

This approach utilizes a dictionary to calculate and store the digit sums of each number in the list, and then sorts the dictionary keys based on the sum of their corresponding values, using the index as a tiebreaker. The sorted keys are then used to rebuild the desired sorted list. This solution is more efficient as it avoids the overhead of multiple loops and simplifies the sorting process, while still adhering to the specified criteria.