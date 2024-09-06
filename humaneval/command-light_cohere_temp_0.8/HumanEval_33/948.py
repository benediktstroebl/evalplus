```python
def sort_third(lst):
    """This function sorts a list l such that the values at positions that are not divisible by three are in l are in the same relative order, while the values at positions that are divisible by three are equal to the values at the corresponding positions of l, but are sorted.
    
    """First, we sort all values of l by default. Then we identify the time divisible by three values in l and sort those values to be equal to the values of l but in reverse order.
    Finally, we need to compare the values at the same position in the list to identify the values divisible by three and sort them accordingly.
    """In the area for the same values of l but in reverse order."""
def test_sort_third(lst):
    """This function tests the sort_third function by passing the list l and checking if the returned list is sorted by the values that are not divisible by three.

    """We check if the both lists have the same values, but the values at the positions that are divisible by three are in the opposite order between the two lists."""
    return sorted(lst) == [2, 6, 3, 4, 8, 9, 5]
```