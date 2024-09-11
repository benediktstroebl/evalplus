```markdown
## pairs_sum_to_zero function
### Description
This function checks for pairs of distinct elements in a list that sum to zero.

### Code
```python
def pairs_sum_to_zero(lst):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

    Args:
        lst (list): A list of integers.

    Returns:
        bool: True if two distinct elements sum to zero, False otherwise.
    """
    # Create a set to store the elements we've seen so far
    seen = set()
    
    # Iterate over the list
    for num in lst:
        # If the negation of the current number is in the set, we've found a pair
        if -num in seen:
            return True
        # Otherwise, add the current number to the set
        seen.add(num)
    
    # If we've iterated over the entire list and haven't found a pair, return False
    return False

# Example usage:
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

### Explanation
This function uses a set to keep track of the elements it's seen so far. It iterates over the list, and for each element, it checks if its negation is in the set. If it is, it means we've found a pair that sums to zero, so it returns True. If it hasn't found a pair after iterating over the entire list, it returns False. This solution runs in O(n) time, where n is the length of the list, making it efficient for large lists.