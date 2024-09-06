```python
def sort_third(lst):
    # Create a list of list of tuples
    flat = list(map(list, lst))

    # Sort list of tuples
    flat.sort()

    # Convert list of tuples back to list of elements
    lst = [tuple(element) for element in flat]

    # Filter out values divisible by three
    lst = [element for element in lst if not(element % 3)]

    return lst

# Unit tests
def test_sort_third():
    test_lst = [5, 6, 3, 4, 8, 9, 2]
    expected = [2, 6, 3, 4, 8, 9, 5]
    result = sort_third(test_lst)
    assert result == expected
```