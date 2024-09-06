```python
def sort_even(l: list):
    """Sorts list l so that elements at odd positions are kept as they are, and the
    elements at even positions are sorted.
    
    Args:
    l (list): list to be sorted
    """
    l.sort(reverse=True)
    return l

# Test the function with some sample inputs
test_list = [1, 2, 3]
test_list.sort_even(test_list)
print("Sorted even numbers:", test_list[1:])

test_list = [5, 6, 3, 4]
test_list.sort_even(test_list)
print("Sorted even numbers:", test_list[1:])
```