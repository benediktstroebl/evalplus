```python
def pairs_sum_to_zero(nums):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

    :param nums: A list of integers
    :return: True if two distinct elements sum to zero, False otherwise
    """
    seen = set()
    for num in nums:
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

This script defines a function `pairs_sum_to_zero` that takes a list of integers as input and returns `True` if there are two distinct elements in the list that sum to zero, and `False` otherwise. The function uses a set `seen` to keep track of the numbers it has seen so far. For each number `num` in the input list, it checks if `-num` (the complement of `num`) is in the `seen` set. If it is, it means that `num` and its complement sum to zero, so the function returns `True`. If it doesn't find any such pair after checking all numbers, it returns `False`.