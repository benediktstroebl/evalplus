```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted."""

    # create a copy of list l
    l_copy = list(l)

    # sort the list such that 3's and 6's are together in the end
    l_copy.sort_by_key('3', l_copy)

    # now that l_copy is sorted, we want to remove the items that are not divisible by three
    # do this by using list.remove()
   
    remove the . non-3rd element(s) from l_copy
    l_copy.remove('3_third_value')

    # return the copy of list l after applying the sort_by_key() function
    return l_copy

# Test the function

# Test list with divisible numbers and non-divisible numbers
test_list = [1, 2, 3, 4, 5, 6, 8, 9, 10]
test_list = sort_third(test_list)
print(test_list)  # Output: [2, 3, 3, 4, 5, 6, 8, 9, 10]
```