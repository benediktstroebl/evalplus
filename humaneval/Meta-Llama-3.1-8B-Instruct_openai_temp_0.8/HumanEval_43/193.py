```python
def pairs_sum_to_zero(lst):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    
    Args:
        lst (list): A list of integers.
    
    Returns:
        bool: True if there are two distinct elements in the list that sum to zero, False otherwise.
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

In this script, we use a set `seen` to keep track of the numbers we have seen so far. For each number `num` in the input list, we check if `-num` is in the `seen` set. If it is, it means we have found two numbers that sum to zero and we return `True`. If we have iterated over the entire list without finding any such pair, we return `False`. This approach has a time complexity of O(n) and a space complexity of O(n) due to the use of the `seen` set.