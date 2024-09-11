Here's a Python script that uses a set data structure to solve the problem efficiently. The set data structure in Python allows us to check if an element exists in O(1) time on average, so we can iterate over the list once and check for pairs summing to zero in a single pass.

```python
def pairs_sum_to_zero(lst):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    num_set = set()
    
    # Iterate over the list
    for num in lst:
        # If the negation of the current number is in the set, return True
        if -num in num_set:
            return True
        # Otherwise, add the current number to the set
        num_set.add(num)
    
    # If we've iterated over the entire list and haven't found a pair summing to zero, return False
    return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script runs in O(n) time and uses O(n) space, where n is the number of elements in the input list. It first initializes an empty set `num_set` to store the numbers we've seen so far. Then, it iterates over the list. For each number `num`, it checks if `-num` is in `num_set`. If it is, it immediately returns `True` because we've found a pair of numbers that sum to zero. If it's not, it adds `num` to `num_set`. Finally, if we've iterated over the entire list without finding a pair summing to zero, we return `False`.