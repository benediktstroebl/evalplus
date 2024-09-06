```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    pair with smaller value is always preferred first.
    """
    time complexity: O(n)
    """
    if len(l) < 2:
        return False
    #First, we will compare the second element with the first one
    smaller = l[1] - l[0]
    if smaller < 0:
        return False
    #Then we will check the third element against the pair before
    larger = l[2] - l[1]
    if larger < 0:
        return False
    #Then we will check the fourth element against the larger pair
    smaller = l[3] - l[2]
    if smaller < 0:
        return False
    #Finally, if all elements are greater than the pair before, then we have a solution
    return True
    #return False
    return False

#test cases
assert pairs_sum_to_zero([1, 3, 5, 0]) == False
assert pairs_sum_to_zero([1, 3, -2, 1]) == False
assert pairs_sum_to_zero([1, 2, 3, 7]) == False
assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
assert pairs_sum_to_zero([1]) == False
```