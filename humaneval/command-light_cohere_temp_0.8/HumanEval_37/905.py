```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the odd indic, while its values at the even indices are equal to the values of the even indicies of l, but sorted."""
    return sorted(l,key=lambda x:x%2)
# tests
print(sort_even([1,2,3]))=[1,2,3]
print(sort_even([5,6,3,4]))=[3,6,5,4]
print(sort_even([-5,8,9,11]))=[-5,8,9,11]
print(sort_even([23,67,90,123]))=[123,90,67,23]
```