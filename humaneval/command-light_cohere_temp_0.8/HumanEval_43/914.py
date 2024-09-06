```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
	"""
    # sort the list
    l.sort()
    sort the fast by applying the sort function to numbers only
    # get first and last element in sorted list
    first, = l[:]
    last, = l[-1]
    # check sum of first and last elements to zero
    if (first[0] + last[0]) == 0:
        return True
    else:
        return False
    """

# test function with list of numbers
test_list = [1, 3, 5, 0]
if pairs_sum_to_zero(test_list):
    print("The list has two numbers that sum to zero.")
else:
    print("The list does not have two numbers that sum to zero.")
```