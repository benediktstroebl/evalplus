Here's a Python script using the provided code as an example. It uses a set to store the numbers we've seen so far and checks if the negative of each number is in the set.
```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    # Create an empty set to store the numbers we've seen so far
    seen = set()
    
    # Iterate over the list
    for num in l:
        # Check if the negative of the current number is in the set
        if -num in seen:
            # If it is, return True
            return True
        # Add the current number to the set
        seen.add(num)
    
    # If we've iterated over the entire list and haven't found a pair
    # that sums to zero, return False
    return False

# Test the function
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```
This script uses a set to store the numbers we've seen so far, which allows us to check if the negative of each number is in the set in constant time. This makes the function more efficient for large input lists.