```python
def pairs_sum_to_zero(lst):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

    :param lst: A list of integers.
    :return: True if two distinct elements sum to zero, False otherwise.
    """
    seen = set()
    for num in lst:
        complement = -num
        if complement in seen:
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
This script defines a function `pairs_sum_to_zero` that takes a list of integers as input. It iterates over the list and checks if the complement of each number (i.e., the number that would sum to zero with it) is already in the set `seen`. If it finds such a pair, it immediately returns `True`. If it finishes iterating over the list without finding a pair, it returns `False`. The test cases at the end verify that the function behaves correctly according to the doctests.