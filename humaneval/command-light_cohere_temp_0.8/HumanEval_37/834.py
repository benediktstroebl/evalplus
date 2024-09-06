```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even index of l, but sorted.
    """
    test: l[:] != l and return Early error."""
    l[:] = [x for x in l if x%2==0] + [x for x in l if x%2!=0]
    return l

# Test the function
test_list = [1,2,3,4,5,6]
print(sort_even(test_list)) 
```