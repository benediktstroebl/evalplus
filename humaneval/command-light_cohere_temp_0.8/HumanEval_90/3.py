```python
def next_smallest(lst):
    if not in lst:  # If empty list
        return None
    lst.remove(lst[-1])  # Remove last element
    return lst[-1]  # Return the smallest element

# Example usage:
test_next_smallest([5, 1, 4, 3, 2])  # Should return 2
test_next_smallest([1])  # Should return 1
test_next_smallest([1, 1])  # Should return 1
test_next_smallest([])  # Should return None
test_next_smallest([5, 6, 2, 3, 1])  # Should return 2
```  This script defines a function `next_smallest` which removes the last element of a list and returns the smallest element in the remaining list.  This This a smaller list can be more efficient for some specific problems, like this one.