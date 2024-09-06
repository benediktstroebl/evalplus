```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.
    """
def test_sort_third(test_list):
        test_list[:] = [3, 6, 9, 5, 2, 4, 8]
        assert sort_third(test_list) == [2, 6, 3, 4, 8, 9, 5]
        test_list[1:]= [10, 11]
        assert sort_third(test_list) == [2, 10, 11, 6, 3, 4, 8]
        test_list[5:] = [7, 8]
        assert sort_third(test_list) == [2, 10, 11, 6, 7, 8, 4]
        return
```