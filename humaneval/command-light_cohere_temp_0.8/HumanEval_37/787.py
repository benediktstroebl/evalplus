```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even indicies of l, but sorted.
    """
    [1, 2, 3]
    [1, 2, 3]
    """
    even = []
    for n in l:
        if n % 2 == 0:
            even.append(n)
    else:
            pass
    even.append(n)
    return even
def test_sort_even():
    # test list
    test_list = [5, 6, 3, 4]
    expected = [3, 6, 5, 4]
    result = sort_even(test_list)
    assert result == expected
```