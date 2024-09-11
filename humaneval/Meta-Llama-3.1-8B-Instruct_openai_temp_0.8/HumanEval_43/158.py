```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that sum to zero, and False otherwise.
    
    Parameters:
    l (list): A list of integers.
    
    Returns:
    bool: True if two distinct elements sum to zero, False otherwise.
    """
    # Create a set to store unique elements from the list
    unique_elements = set()
    
    # Iterate over the list
    for num in l:
        # Check if the negative of the current number is in the set
        if -num in unique_elements:
            # If the negative of the current number is in the set, return True
            return True
        # Add the current number to the set
        unique_elements.add(num)
    
    # If the function hasn't returned True, return False
    return False


# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script defines a function `pairs_sum_to_zero` that checks if there are two distinct elements in a list that sum to zero. It uses a set to store unique elements from the list and iterates over the list to check for pairs that sum to zero. If such a pair is found, the function returns `True`; otherwise, it returns `False`. The script includes test cases to verify the correctness of the function.