```markdown
## pairs_sum_to_zero Function
### Description
This function checks if there are two distinct elements in a list that sum to zero.
### Code
```python
def pairs_sum_to_zero(lst):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

    Parameters:
    lst (list): A list of integers.

    Returns:
    bool: True if there are two distinct elements that sum to zero, False otherwise.
    """
    # Create a set to store the elements we've seen so far
    seen = set()
    
    # Iterate over the list
    for num in lst:
        # Check if the negative of the current number is in the set
        if -num in seen:
            # If it is, return True because we've found two numbers that sum to zero
            return True
        # If not, add the current number to the set
        seen.add(num)
    
    # If we've iterated over the entire list and haven't found two numbers that sum to zero, return False
    return False

# Example use cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```
### Explanation
This function uses a set to keep track of the numbers we've seen so far. It iterates over the list and checks if the negative of the current number is in the set. If it is, the function returns True because we've found two numbers that sum to zero. If not, the function adds the current number to the set and continues iterating. If we've iterated over the entire list and haven't found two numbers that sum to zero, the function returns False.
### Time Complexity
The time complexity of this function is O(n) where n is the number of elements in the list, because we're doing a constant amount of work for each element in the list.
### Space Complexity
The space complexity of this function is also O(n) in the worst case, because we're storing all the elements in the list in the set.