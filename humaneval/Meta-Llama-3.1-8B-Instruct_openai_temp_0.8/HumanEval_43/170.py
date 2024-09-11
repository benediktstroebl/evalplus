### Solution
```python
def pairs_sum_to_zero(lst):
    """
    Returns True if there are two distinct elements in the list that sum to zero, and False otherwise.

    Args:
        lst (list): A list of integers.

    Returns:
        bool: Whether two distinct elements in the list sum to zero.

    Examples:
        >>> pairs_sum_to_zero([1, 3, 5, 0])
        False
        >>> pairs_sum_to_zero([1, 3, -2, 1])
        False
        >>> pairs_sum_to_zero([1, 2, 3, 7])
        False
        >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
        True
        >>> pairs_sum_to_zero([1])
        False
    """
    seen = set()
    for num in lst:
        if -num in seen:
            return True
        seen.add(num)
    return False
```

### Explanation
This solution works by iterating over the list and using a set to keep track of the numbers we have seen so far. If we encounter a number that is the negative of a number we have seen before, we immediately return True, because we have found a pair of numbers that sum to zero. If we finish iterating over the list without finding such a pair, we return False. The time complexity of this solution is O(n), where n is the length of the list, because we are doing a constant amount of extra work for each element in the list.