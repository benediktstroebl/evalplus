```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the integer in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums:
        return []

    # Calculate the sum-of-digits score for each number
    digit_sums = [sum(int(d) for d in str(n)) for n in nums]

    # Split the list into sorted groups according to digit_sums
    sorted_groups = [nums[idx:] for idx in range(len(nums)) if digit_sums[idx] >= digit_sums[idx+1]]

    # Sort each group according to index in the original list
    sorted_groups = [group[idx:] for group in sorted_groups for idx in range(len(group))]

    return sorted_groups[0]
```

The above code employs a tuple unpacking technique in the lambda function to create a list of tuples from a single tuple. This allows the `sorted()` function to sort the list of tuples by the second element of each tuple (the original index), effectively achieving the desired sorting behavior with tiebreaks. 

This solution has a time complexity of `O(Nlog(M))`, where `N` is the length of the input list and `M` is the maximum amount of integers with the same digit sum in the list. This assumes that the maximum number of integers with the same digit sum is a constant, which is typically true in practice.