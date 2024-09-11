```python
def pairs_sum_to_zero(nums):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

    Args:
        nums (list): A list of integers.

    Returns:
        bool: True if two distinct elements sum to zero, False otherwise.
    """
    seen = set()  # stores the numbers we have seen so far
    for num in nums:
        if -num in seen:  # check if the negative of the current number is in seen
            return True  # if it is, then we have found a pair that sums to zero
        seen.add(num)  # otherwise, add the current number to seen
    return False  # if we have iterated over the entire list and not found a pair, return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script defines a function `pairs_sum_to_zero` that checks if there are two distinct elements in a list that sum to zero. It uses a set `seen` to keep track of the numbers it has seen so far, and checks if the negative of each number is in `seen`. If it is, then it returns `True`. If it has iterated over the entire list without finding a pair, it returns `False`. The test cases are included at the end of the script.