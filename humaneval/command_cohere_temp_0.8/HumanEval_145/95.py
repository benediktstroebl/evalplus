```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers based on index.

    Args:
        nums (list): List of integers

    Returns:
        list: Ordered list based on the criteria specified.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums:
        return []

    # Calculate the digit-sum-ordered index for each number
    key = lambda x: (sum(int(d) for d in str(x)), nums.index(x))

    # Sort the list based on the key
    return sorted(nums, key=key)
```

This approach utilizes a lambda function as the sorting key, which first calculates the sum of the digits of each number and then relies on the index of the number in the original list as a tiebreaker. Using this lambda function, the `sorted` function is used to sort the original list. Additionally, the code checks for an empty input list and returns an empty list if necessary.

You can verify the correct operation of the function using the provided tests in the original problem statement.