```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal
    to the values of the even index of l, but sorted."""
    l[:2] = [x for x in l[1:]] + [l[0]]
    l[2:] = [l[0]] + [x for x in l[1:]]
    return l

#Test the function
# [2, 3, 4, 5, 6] is the odd list, and [3, 4, 5, 6] is the even list
test_result = sort_even([2, 3, 4, 5, 6])
print(test_result)
[3, 4, 5, 6]
```