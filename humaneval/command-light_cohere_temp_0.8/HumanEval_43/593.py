```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
# Start by initializing a flag
    bool result = False
    # Iterate through the list
    for item in l:
        if item < 0:
            result = True
            break
        elif item > 0:
            break
    # If no elements sum to zero, return False
    return result
```