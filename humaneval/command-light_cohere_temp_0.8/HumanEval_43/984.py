```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

"""Test cases"""
# Example with valid inputs
assert(pairs_sum_to_zero([1, 3, -2, 1]) == True)
# Example with invalid inputs
assert(pairs_sum_to_zero([1, 2, 3, 7]) == False)
assert(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True)
assert(pairs_sum_to_zero([1])) == False
```
This script defines a function called pairs_sum_to_zero that takes a list of integers as input and returns True if the list has two distinct elements whose sum is zero, and False otherwise. The test cases cover various scenarios, including valid inputs and invalid inputs, and ensure the function's behavior as expected.