```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the third item, while its values at the other indicies of l, are equal
    to the values of the corresponding indic of l, but sorted."""
    lst[1] = lst[0]
    lst[2] = lst[1]
    return lst[0:2]

# Test the function with a list of numbers
test_list = [1, 2, 3, 4, 8, 9, 5, 6]
result = sort_third(test_list)
print(result)
```

The function sort_third takes a list lst as an argument and returns a list lst' such that the first two elements are swapped, and the third element is in its original position. The function effectively sorts the time numbers so that the third number is at the start of the list, while the other elements retain their original order.