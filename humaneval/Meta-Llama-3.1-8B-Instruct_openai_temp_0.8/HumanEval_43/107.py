### pairs_sum_to_zero Function
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
    seen = set()  # Create an empty set to store the elements we have seen so far
    for num in l:
        if -num in seen:  # If the negative of the current number is in the set, we have found a pair that sums to zero
            return True
        seen.add(num)  # Add the current number to the set
    return False  # If we have iterated over the entire list and haven't found a pair, return False
```

### Example Use Cases
```python
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This function works by iterating over the input list and using a set to keep track of the elements we have seen so far. If we encounter a number whose negative is already in the set, we have found a pair that sums to zero, so we return True. If we have iterated over the entire list and haven't found a pair, we return False.