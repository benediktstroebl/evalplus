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

This script defines a function `pairs_sum_to_zero` that takes a list of integers as input. It iterates over the list and for each number, it checks if its negation is in the `seen` set. If it is, the function returns `True`, indicating that there is a pair of numbers that sum to zero. If it's not, the function adds the current number to the `seen` set and continues iterating. If it finishes iterating without finding a pair, it returns `False`.

The time complexity of this function is O(n), where n is the length of the list, because it uses a set to keep track of the numbers it has seen so far, which allows it to check if a number is in the set in constant time. The space complexity is also O(n), because in the worst case, the function has to store all numbers in the list in the `seen` set.