```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    # Create an empty set to store the elements we have seen so far
    seen = set()
    
    # Iterate over the list
    for num in l:
        # Check if the negative of the current number is in the set
        if -num in seen:
            # If it is, return True because we have found a pair that sums to zero
            return True
        # If not, add the current number to the set
        seen.add(num)
    
    # If we have iterated over the entire list and haven't found a pair, return False
    return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script uses a set to keep track of the elements we have seen so far. The time complexity is O(n) where n is the number of elements in the list because each element is added to the set and checked once. The space complexity is also O(n) because in the worst case we might have to store all elements in the set.