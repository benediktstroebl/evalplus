```python
def sort_third(lst):
    """Sorts list l such that values not divisible by three stay as they are, and all other values are sorted.
    
    Args:
    lst (list): a list of integers
    Returns:
    lst (list): a sorted list of integers
    """
    import sorting
    lst.sort(algorithm='mergesort')
    return lst

# Unit tests
def test_sort_third():
    assert sort_third([1, 2, 3]) == [1, 2, 3]
    assert sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]

# Example usage
print(test_sort_third())
 ```