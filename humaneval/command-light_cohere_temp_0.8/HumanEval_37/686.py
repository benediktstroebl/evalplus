```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indic, while its values at the even indic are equal
    to the values of the even indic of l, but sorted.
    """
    test:
    assert len(l)==2, "list must contain 2 elements"
    assert l[0]%2==0 and l[1]%2==0, "elements must be even"
    assert sorted(l)==l,'Given list is not sorted'
    return l

test_even = []
test_even.add(sort_even([1,2]))
test_even.add(sort_even([5,6]))
test_even.add(sort_even([3,4]))

print(test_even)
```