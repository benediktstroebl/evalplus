```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    list comprehension is very straightforward way to solve this problem:
        return any(sum([x for x in l]) == 0)
    """

def test():
    """
    Test function for pairs_sum_to_zero.
    Test if the set 1, 3, 5, 0 and 1 are in pairs_sum_to_zero([1, 3, -2, 1])
        then the function is successful.

# Test the function with some inputs
test()
pairs_sum_to_zero([1, 3, -2, 1]) # True
pairs_sum_to_zero([1, 2, 3, 7]) # False
pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) # True
pairs_sum_to_zero([1]) # False
```