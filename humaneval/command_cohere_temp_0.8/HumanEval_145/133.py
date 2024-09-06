```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tie breaks determined by the index of the integer in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Sortedd list based on criteria.
    """
    if not nums:
        return []

    summed_digits = []
    original_indices = [i for i, n in enumerate(nums)]

    for n in nums:
        sum_digits = sum(int(d) for d in str(n))
        summed_digits.append((sum_digits, i))

    # Sort based on sum of digits with tie breaks based on original index
    sorted_nums = sorted(nums, key=lambda n: summed_digits.index(
        (summed_digits.count(n[0]), n[1])))

    return sorted_nums
```

The approach used in the code is a hybrid of two types of sorting:
1. **Digit-sum sorting**: This is used as the primary sorting metric, akin to sorting by ' hashCode' in Java or 'toString()' in Java or Python, with the tie-breaker.
2. **Index-based sorting**: This is used as the tie-breaker metric, akin to sorting by 'compareTo' in Java or the intrinsic 'cmp' function in Python. This approach minimizes the likelihood of duplicate elements at the same depth, which would induce non-determinism.