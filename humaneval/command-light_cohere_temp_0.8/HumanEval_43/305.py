```python
def pairs_sum_to_zero(l):
    """
    A function to check if a list of integers sums to zero.
    """
    returns: True, if there are two distinct elements in the list that sum to zero, otherwise False."""
    
    # Initialize sum of elements
    sum_ = 0
    
    # Initialize counter for two distinct elements
    count = 0
    
    for num in l:
        sum_ += num
        count += 1
        
    return count == 2 and sum_==0 else False

# Example usage
>>> pairs_sum_to_zero([1, 3, 5, 0]) # True
>>> pairs_sum_to_zero([1, 3, -2, 1]) # False
>>> pairs_sum_to_zero([1, 2, 3, 7]) # False
>>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) # True
>>> pairs_sum_to_zero([1]) # False
```