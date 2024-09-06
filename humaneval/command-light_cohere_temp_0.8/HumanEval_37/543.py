```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even indicies of l, but sorted.
    """
    def test(test_list):
        test_list[:] = [3, 2, 4, 5, 6]
        expected = [3, 4, 5, 6]
        got = sort_even(test_list)
        return expected == got
    return sorted(l)
test_func = test
```