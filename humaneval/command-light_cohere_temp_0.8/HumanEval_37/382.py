```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indic of l, but sorted.
    :param l: list - A list of numbers.
    :return: list, where the even index is sorted in ascending order, and the odd index is sorted in descending order.
    """
    test: 
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert sort_even([10, 20, 30]) == [30, 10, 20]
    assert sort_even([10, 11, 100]) == [100, 10, 11]
    assert sort_even([-5, 6, -3]) == [-3, -5, 6]
    assert sort_even([1, -2, 3]) == [-2, -1, 3]
    assert sort_even([10, 20, 30, 40]) == [30, 20, 10, 40]
    """
```