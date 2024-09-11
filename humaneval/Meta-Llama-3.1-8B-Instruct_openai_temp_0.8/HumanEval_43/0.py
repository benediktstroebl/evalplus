### pairs_sum_to_zero Function

Below is a Python function that fulfills the specified requirements:

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

### Explanation

This function uses a set called `seen` to store the elements we have already seen. It iterates over the list, and for each element, it checks if the additive inverse of the current element (i.e., `-num`) exists in the `seen` set. If it does, the function immediately returns `True` because we have found two distinct elements that sum to zero.

If we have iterated over the entire list without finding any such pair, the function returns `False` because there are no two distinct elements that sum to zero.

### Time Complexity

The time complexity of this function is O(n), where n is the number of elements in the list, because we make a single pass over the list. The space complexity is also O(n) because in the worst case, we might need to store all elements in the `seen` set.