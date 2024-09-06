```python
def sort_third(lst):
    """Sorts a list such that the values at indices that are not divisible by three are in the beginning, and the corresponding values at the other indices are equal to the values of the corresponding indices of the original list, but sorted."""

    return lst."""
    def test_sort_third(self):
        lst = [1, 2, 3]
        self.sort_third(lst)
        assert lst == [1, 2, 3]
        lst = [5, 6, 3, 4, 8, 9, 2]
        self.sort_third(lst)
        assert lst == [2, 6, 3, 4, 8, 9, 5]
```