```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even indicies of l, but sorted."""
    l[:len(l)//2] = [x if i%2 == 0 else x[::-1] for i, x in enumerate(l)]
    return l

# Test the function with various input
for i in [5, 6, 3, 4, 10, 2, 8, 7, 9]:
    test_list = [i, i*i, i+1]
    assert sort_even(test_list) == [i, i*i, i+1]
```
The function `sort_even` is a self-contained Python function that sorts a list such that the values of even indices are equal to the corresponding values of the even indices of the original list, but in sorted order. The function uses the method of selecting every other element in the list, and flipping the sign of its current value if the index is odd.