```python
def pairs_sum_to_zero(l):
    """
    returns True if there are two distinct elements in the list that sum to zero, 
    and False otherwise.
    """
    uses python's assert statement inside the function to test if the condition is met. 

Example usage: 
    print(pairs_sum_to_zero([1, 3, 5, 0])) # False
    print(pairs_sum_to_zero([1, 3, -2, 1])) # False
    print(pairs_sum_to_zero([1, 2, 3, 7])) # False
    print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7])) # True
    """

# Test cases
assert pairs_sum_to_zero([1, 3, 5, 0]) == False
assert pairs_sum_to_zero([1, 3, -2, 1]) == False
assert pairs_sum_to_zero([1, 2, 3, 7]) == False
assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
assert pairs_sum_to_zero([1]) == False
```