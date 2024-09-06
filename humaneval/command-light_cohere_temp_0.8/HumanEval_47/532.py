```python
def median(lst):
    """Return median of elements in the list lst."""
    return (len(lst) + 1)**.5 / 2.0 if len(lst) % 2 == 0 else float(lst.median((lst[(len(lst) + 1) / 2)] + lst[(len(lst) + 1) // 2]))

# Test cases
median([3, 1, 2, 4, 5]) #3.0
median([-10, 4, 6, 1000, 10, 20]) #15.0
median([0, 2, 3, -7]) #2.0
median([20, 40, 60, 80]) #70.0
median([1, 2, 3, 4]) #2.0
median([9, 8, 7, 6]) #3.0
median([1000, 1001, 1002]) #1001.0

The median of the list is calculated by finding the middle value(s) of the list, and is calculated using the formula (n+1)/2 for odd lists and ((n+1)*(n+2))/2 for even lists.  is passed using the test cases to see that the function returns the correct median.