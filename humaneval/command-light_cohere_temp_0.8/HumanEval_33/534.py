```python
def sort_third(lst):
    """Sorts the list l such that the values at positions divisible by three are in their correct relative order."""
    return sorted(lst, key=lambda x:int(x)//3 if x%3 else x)

# Unit tests
def test_sort_third():
    assert sort_third([1,2,3]) == [1, 2, 3]
    assert sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
    assert sort_third([10, 20, 30]) == [10, 20, 30] # Should order as 30, 20, 10
    assert sort_third([50, 30, 20, 10]) == [50, 30, 20, 10] # Should order as 50, 30, 20, 10
```