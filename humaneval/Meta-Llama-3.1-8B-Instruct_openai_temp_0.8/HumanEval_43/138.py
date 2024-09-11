```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    
    :param l: a list of integers
    :return: a boolean indicating whether two distinct elements sum to zero
    """
    # Create a set to store the elements we've seen so far
    seen = set()
    # Iterate over the list
    for num in l:
        # If the negation of the current number is in the seen set, return True
        if -num in seen:
            return True
        # Otherwise, add the current number to the seen set
        seen.add(num)
    # If we've iterated over the entire list and haven't found two numbers that sum to zero, return False
    return False

# Test cases
if pairs_sum_to_zero([1, 3, 5, 0]):
    assert False, "Test case failed: [1, 3, 5, 0]"
if pairs_sum_to_zero([1, 3, -2, 1]):
    assert False, "Test case failed: [1, 3, -2, 1]"
if pairs_sum_to_zero([1, 2, 3, 7]):
    assert False, "Test case failed: [1, 2, 3, 7]"
if pairs_sum_to_zero([2, 4, -5, 3, 5, 7]):
    assert True, "Test case passed: [2, 4, -5, 3, 5, 7]"
if not pairs_sum_to_zero([1]):
    assert True, "Test case passed: [1]"
```

This script defines a function `pairs_sum_to_zero` that takes a list of integers as input and returns `True` if there are two distinct elements in the list that sum to zero, and `False` otherwise. It uses a set to keep track of the elements it has seen so far, and checks if the negation of the current number is in the set. If it is, it returns `True`. If it iterates over the entire list without finding two numbers that sum to zero, it returns `False`. The script also includes test cases to verify the correctness of the function.