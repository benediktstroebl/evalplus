```python
def pairs_sum_to_zero(lst):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    
    Args:
        lst (list): A list of integers.
    
    Returns:
        bool: True if there are two distinct elements that sum to zero, False otherwise.
    """
    seen = set()
    for num in lst:
        if -num in seen:
            return True
        seen.add(num)
    return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script uses a set `seen` to store the numbers it has seen so far. For each number `num` in the input list, it checks if `-num` is in `seen`. If it is, it means that `num` and `-num` sum to zero, so it returns `True`. If not, it adds `num` to `seen` and continues. If it has iterated over the entire list without returning `True`, it returns `False`. This approach has a time complexity of O(n), where n is the length of the input list.