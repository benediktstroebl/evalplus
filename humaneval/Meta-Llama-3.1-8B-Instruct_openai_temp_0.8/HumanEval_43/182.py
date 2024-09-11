```python
def pairs_sum_to_zero(lst):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    # Create a set to store the numbers we've seen so far
    num_set = set()
    
    # Iterate over the list
    for num in lst:
        # Check if the negation of the current number is in the set
        if -num in num_set:
            # If it is, return True
            return True
        # If not, add the current number to the set
        num_set.add(num)
    
    # If we've iterated over the entire list and haven't found a pair that sums to zero, return False
    return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script uses a set to store the numbers we've seen so far. It iterates over the list, and for each number, it checks if its negation is in the set. If it is, it returns True, because we've found a pair that sums to zero. If we reach the end of the list without finding such a pair, it returns False. This approach has a time complexity of O(n), where n is the length of the list.