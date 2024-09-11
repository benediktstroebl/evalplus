```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

    Args:
        l (list): A list of integers.

    Returns:
        bool: True if two distinct elements sum to zero, False otherwise.
    """
    seen = set()  # A set to store the numbers we've seen so far
    for num in l:  # Iterate over the list
        complement = -num  # The number that, when added to num, gives 0
        if complement in seen:  # If we've seen the complement before
            return True  # We've found two numbers that sum to zero
        seen.add(num)  # If not, add the current number to the set
    return False  # If we've iterated over the entire list and found no pairs, return False


# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script defines a function `pairs_sum_to_zero` that takes a list of integers as input and returns `True` if there are two distinct elements in the list that sum to zero, and `False` otherwise. It uses a set to keep track of the numbers it has seen so far and checks whether the complement of the current number (i.e., the number that, when added to the current number, gives 0) is in the set. If it is, the function returns `True`. If the function iterates over the entire list without finding any pairs of numbers that sum to zero, it returns `False`. The script includes test cases to demonstrate the function's behavior.