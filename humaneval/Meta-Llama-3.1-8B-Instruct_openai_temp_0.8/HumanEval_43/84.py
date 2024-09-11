```markdown
### pairs_sum_to_zero Function

#### Description
This function determines whether a given list of integers contains two distinct elements that sum to zero.

#### Code
```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    
    Parameters:
    l (list): A list of integers.
    
    Returns:
    bool: True if there are two distinct elements in the list that sum to zero, False otherwise.
    """
    seen = set()  # Use a set to store elements we've seen so far
    for num in l:
        complement = -num  # Calculate the complement of the current number
        if complement in seen:  # Check if we've seen the complement before
            return True  # Return True if we have, indicating a pair that sums to zero
        seen.add(num)  # Add the current number to the set of seen numbers
    return False  # If we've iterated over the entire list without finding a pair, return False

### Example Use Cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

#### Explanation
This function uses a set to keep track of elements we've seen so far. We iterate over the input list, and for each number, we calculate its complement (the number that would need to be added to it to get zero). If the complement is already in the set of seen numbers, we return True, indicating that we've found a pair that sums to zero. If we iterate over the entire list without finding a pair, we return False.

This function has a time complexity of O(n), where n is the length of the input list, because we're doing a constant amount of work for each element in the list. The space complexity is also O(n), because in the worst case (when all numbers are unique), we'll be storing all elements in the set of seen numbers.