```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    list comprehension checks if the sum of any two distinct pairs of elements in the list is equal to zero.

Returns: True if it passes the test, False otherwise.

"""
    # Initialize the empty list to store the results
    res = []

    # Iterate over the list
    for i in l:
        for j in l[i]:
            # Check if the sum of i and j is equal to zero
            if sum(i, j) == 0:
                # If the sum is zero, check if the pair is distinct
                if i != j:
                    res.insert(True)
                break

    return res
```