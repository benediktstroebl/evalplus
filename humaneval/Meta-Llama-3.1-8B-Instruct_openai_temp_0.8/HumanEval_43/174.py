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
    seen = set()  # keep track of the elements we've seen so far
    for num in lst:
        complement = -num  # the complement of a number is the number that added to it equals zero
        if complement in seen:  # if we've seen the complement before
            return True  # then we've found two numbers that sum to zero
        seen.add(num)  # otherwise, add the current number to the set of seen numbers
    return False  # if we've iterated over the entire list and haven't found a pair of numbers that sum to zero, return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script defines a function `pairs_sum_to_zero` that takes a list of integers as input and returns `True` if there are two distinct elements in the list that sum to zero, and `False` otherwise. The function uses a set to keep track of the elements it has seen so far, and it iterates over the input list to find a pair of numbers that sum to zero. If it finds such a pair, it returns `True`; otherwise, it returns `False`. The script includes test cases to demonstrate the function's behavior.