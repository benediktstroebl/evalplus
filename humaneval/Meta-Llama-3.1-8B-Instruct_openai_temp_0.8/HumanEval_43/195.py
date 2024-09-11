```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    
    Parameters:
    l (list): A list of integers.
    
    Returns:
    bool: True if two distinct elements sum to zero, False otherwise.
    """
    seen = set()  # Initialize an empty set to keep track of seen elements
    for num in l:  # Iterate over the list
        complement = -num  # Calculate the complement of the current number
        if complement in seen:  # If the complement is in the set of seen elements
            return True  # Return True because two distinct elements sum to zero
        seen.add(num)  # Add the current number to the set of seen elements
    return False  # If no such pair is found, return False


# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))
print(pairs_sum_to_zero([1, 3, -2, 1]))
print(pairs_sum_to_zero([1, 2, 3, 7]))
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))
print(pairs_sum_to_zero([1]))
```

In this script, we use a set `seen` to keep track of the elements we have seen so far. For each element in the list, we calculate its complement (the number that would sum up to zero) and check if it is in the set `seen`. If it is, we return `True` because we have found a pair of distinct elements that sum to zero. If we have iterated over the entire list and not found such a pair, we return `False`.