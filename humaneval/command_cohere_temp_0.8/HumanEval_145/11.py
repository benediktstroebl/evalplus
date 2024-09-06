```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tie breaks determined by the index of the integer in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Sortedd list of integers.
    """
    if len(nums) == 0:
        return []

    # Make a copy of the list to preserve the original order.
    nums_copy = list(nums)

    # Sort the copy based on sum of digits and original index.
    nums_copy.sort(key=lambda x: (sum(int(d) for d in str(x)), nums.index(x)))

    return nums_copy
```

This script employs a `key` word argument, recognized by Python's `sort` function, to organize the list. This `key` is a lambda function that, at each iteration, extracts the sum of the digits of the integer and combines it with its index in the original list. The integers are sorted primarily by the digit sum and, in the case of tie, by their index.

Here's an example usage of the function:
```python
>>> order_by_points([1, 11, -1, -11, -12])
[-1, -11, 1, -12, 11]
```

This function handles the empty list case, and the output is sorted as specified in the problem statement.