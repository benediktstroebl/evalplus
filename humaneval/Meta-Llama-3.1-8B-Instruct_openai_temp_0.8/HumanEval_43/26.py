```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    
    :param l: A list of integers
    :return: True if there are two distinct elements in the list that sum to zero, False otherwise
    """
    # Create a set to store the elements we have seen so far
    seen = set()
    
    # Iterate over the list
    for num in l:
        # For each number, check if its negation is in the seen set
        # If it is, return True because we found a pair that sums to zero
        if -num in seen:
            return True
        # If not, add the number to the seen set
        seen.add(num)
    
    # If we have iterated over the entire list and haven't found a pair that sums to zero, return False
    return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script uses a set to keep track of the numbers we have seen so far. For each number in the list, it checks if its negation is in the set. If it is, it returns True because we have found a pair that sums to zero. If not, it adds the number to the set and continues. If we have iterated over the entire list and haven't found a pair that sums to zero, it returns False.