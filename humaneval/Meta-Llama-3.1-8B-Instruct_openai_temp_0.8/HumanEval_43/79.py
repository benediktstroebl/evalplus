```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

    :param l: A list of integers
    :return: A boolean indicating whether there are two distinct elements
             that sum to zero
    """
    seen = set()  # Use a set to store the elements we've seen so far
    for num in l:
        if -num in seen:  # Check if the negation of the current number is in the set
            return True  # If it is, it means we've found a pair that sums to zero
        seen.add(num)  # Add the current number to the set
    return False  # If we've iterated over the entire list and haven't found a pair, return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script defines a function `pairs_sum_to_zero` that takes a list of integers as input. It uses a set `seen` to keep track of the elements it's seen so far, and checks for each element if its negation is in the set. If it is, it returns `True`, indicating that it's found a pair that sums to zero. If it iterates over the entire list without finding such a pair, it returns `False`. The test cases at the end demonstrate the function's behavior.