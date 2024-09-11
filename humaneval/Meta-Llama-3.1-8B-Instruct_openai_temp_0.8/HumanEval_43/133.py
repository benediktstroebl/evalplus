### Pairs Sum to Zero
#### Problem Description
This script checks if there are two distinct elements in a list that sum to zero.

#### Code
```markdown
def pairs_sum_to_zero(lst):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    
    Args:
        lst (list): A list of integers
    
    Returns:
        bool: Whether there are two distinct elements in the list that sum to zero
    """
    # Create a set to store the numbers we have seen so far
    seen = set()
    
    # Iterate over the list of numbers
    for num in lst:
        # Check if the negation of the current number is in the set
        if -num in seen:
            # If it is, return True
            return True
        # Otherwise, add the current number to the set
        seen.add(num)
    
    # If we have iterated over the entire list and not found a pair of numbers
    # that sum to zero, return False
    return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

#### Explanation
The `pairs_sum_to_zero` function works by iterating over the list of numbers. For each number, it checks if the negation of that number is in the set of numbers it has seen so far. If it is, it returns True, because it has found a pair of numbers that sum to zero. If it hasn't found a pair of numbers that sum to zero after iterating over the entire list, it returns False. The time complexity of this function is O(n), where n is the number of elements in the list, because it performs a constant amount of work for each element in the list. The space complexity is also O(n), because in the worst case it may need to store all of the numbers in the list in the set.