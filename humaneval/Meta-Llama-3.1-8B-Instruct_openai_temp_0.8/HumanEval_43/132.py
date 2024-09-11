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
    # Create a set to store the numbers we've seen so far.
    # This allows us to check if a number's complement is in the set in constant time.
    seen = set()
    
    # Iterate over the list.
    for num in l:
        # Check if the complement of the current number is in the set.
        # If it is, return True because we've found two numbers that sum to zero.
        if -num in seen:
            return True
        # If not, add the current number to the set.
        seen.add(num)
    
    # If we've iterated over the entire list and haven't found two numbers that sum to zero, return False.
    return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script uses a set to keep track of the numbers we've seen so far. It iterates over the list, checking if the complement of each number is in the set. If we find a pair of numbers that sum to zero, we return True. If we don't find any such pair after iterating over the entire list, we return False. This solution has a time complexity of O(n), where n is the length of the list.