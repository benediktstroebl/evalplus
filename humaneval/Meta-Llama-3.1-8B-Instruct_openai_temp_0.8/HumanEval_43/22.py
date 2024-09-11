```markdown
### pairs_sum_to_zero function

This function takes a list of integers as input and returns True if there are two distinct elements in the list that sum to zero, and False otherwise.

#### Code
```python
def pairs_sum_to_zero(lst):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    # Create a set to store the elements we've seen so far
    seen = set()
    
    # Iterate over the list
    for num in lst:
        # If the negation of the current number is in the set, return True
        if -num in seen:
            return True
        # Otherwise, add the current number to the set
        seen.add(num)
    
    # If we've iterated over the entire list and haven't found a pair of numbers that sum to zero, return False
    return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

#### Explanation
This solution uses a set to keep track of the elements we've seen so far. For each number in the list, we check if its negation is in the set. If it is, we return True, because we've found a pair of numbers that sum to zero. Otherwise, we add the current number to the set. If we've iterated over the entire list and haven't found a pair of numbers that sum to zero, we return False. This solution has a time complexity of O(n), where n is the length of the input list.