```python
def sort_third(lst):
    """This function sorts a list so that elements which are divisible by three are in their correct positions,
    while the rest stay in their original order.
    
    Args:
    lst (list)
    
    Returns:
    list, with the above guarantee
    """
    return lst if all(x%3 == 0 for x in lst) else lst[::3] + [x for x in lst if x%3 > 0]

# test cases
test_sort_third = [
    assert sort_third([1, 2, 3]) == [1, 2, 3]
    assert sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
    assert sort_third([5, 6, 9, 3, 4, 8, 2]) == [2, 6, 9, 3, 4, 8, 5]
]
```