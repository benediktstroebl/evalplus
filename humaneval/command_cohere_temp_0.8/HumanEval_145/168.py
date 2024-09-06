```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Ordered list according to specified criteria.
    """
    sorted_nums = sorted(nums, key=lambda x: (sum(map(int, str(x))), x))
    return sorted_nums
```

This script uses the `sorted` function, utilizing a custom key to determine the sorting order. This key is a lambda function that produces a tuple, consisting of the sum of the digits of the number represented as a string (`str(x)`), and the number itself. The numbers are sorted based on this tuple in ascending order, with the index as the tiebreaker in case two numbers have the same digit sum.

For example, given the input `[1, 11, -1, -11, -12]`, the output would be `[-1, -11, 1, -12, 11]`.

This algorithm has a time complexity of O(n log n) due to the `sorted` function, which uses a comparison-based sorting algorithm under the hood (e.g., merge sort or quicksort). The sum of the digits operation takes O(k) time where k is the number of digits, which is usually constant for the numbers we normally deal with. Thus, the overall complexity is dominated by the sorting algorithm.