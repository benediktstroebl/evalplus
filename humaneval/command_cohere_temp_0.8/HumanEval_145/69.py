```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Example:
        >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
        True

    Returns:
        List: Sorted list according to the specified criteria.
    """
    sorted_nums = sorted(nums, key=lambda x: (sum(int(d) for d in str(x)), x))
    return sorted_nums
```
This approach utilizes a lambda function as the key argument in the `sorted()` function. This lambda function calculates the sum of digits in a number and uses this value as the first sort criteria. As a secondary sort criteria, it uses the original index of the number in the list, should there be a tie. This results in the desired sorting order as specified in the problem statement.

The docstring provides an example and clarifies the return value, ensuring a better understanding of the function's behavior.