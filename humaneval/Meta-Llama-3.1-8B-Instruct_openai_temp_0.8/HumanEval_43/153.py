```python
def pairs_sum_to_zero(lst):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    # Create a set for efficient lookups
    num_set = set()
    
    # Iterate over the list
    for num in lst:
        # Check if the complement (which is negated) exists in the set
        if -num in num_set:
            return True
        # Add the current number to the set
        num_set.add(num)
    
    # If no pair with a sum of zero is found, return False
    return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script uses a set to store the numbers it has seen so far. It iterates over the list, and for each number, it checks if its complement (which is the negated number) is in the set. If it is, it returns True because it has found a pair that sums to zero. If it hasn't found any such pair after iterating over the entire list, it returns False. This solution has a time complexity of O(n), where n is the number of elements in the list.