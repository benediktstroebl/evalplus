```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

    Args:
        l (list): A list of integers

    Returns:
        bool: Whether there are two distinct elements that sum to zero
    """
    seen = set()  # a set to store the numbers we've seen so far
    for num in l:  # iterate over the list
        complement = -num  # the number that would sum to zero with num
        if complement in seen:  # if we've seen the complement before
            return True  # then we've found two numbers that sum to zero
        seen.add(num)  # otherwise, add the current number to the set
    return False  # if we've iterated over the whole list and haven't found a pair

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script defines a function `pairs_sum_to_zero` that takes a list of integers as input and returns `True` if there are two distinct elements that sum to zero, and `False` otherwise. The function uses a set to keep track of the numbers it has seen so far, and iterates over the list to find a pair of numbers that sum to zero. If such a pair is found, the function returns `True`; otherwise, it returns `False`. The script also includes test cases to verify the correctness of the function.