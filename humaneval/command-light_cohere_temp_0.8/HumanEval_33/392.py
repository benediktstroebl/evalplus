```python
def sort_third(lst):
    """This function sorts a list l such that elements not divisible by three are at the beginning."""
    return sorted(lst, key=lambda x: (not divisible(x, 3)), reverse=True)

def divisible(x, y):
    """This function checks if x is divisible by y."""
    return y == 0 or x % y == 0

def test_sort_third():
    """This function tests the sort_third function."""
    assert sort_third([1, 2, 3]) == [1, 2, 3]
    assert sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
    assert sort_third([10, 20, 30]) == [10, 20, 30]
    assert sort_third([40, 20, 10]) == [40, 20, 10]

def test_divisible():
    """This function tests the divisible function."""
    assert divisible(2, 4) == True
    assert divisible(2, 5) == False
    assert divisible(3, 5) == True
```
The code provides a self-contained Python script that solves the problem of sorting a list such that elements not divisible by three are at the beginning, and then tests the functions with various inputs.