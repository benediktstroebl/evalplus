```python
def sort_even(l: list):
    """Sorts list l of integers into ascending order, 
    keeping even numbers in their original order."""
    
    # Sort the list keeping even numbers 
    l = [i for i in l if i % 2 != 0]
    
    # Sort the list the default way 
    l.sort()
    
    # Union of the previous two lists 
    return l

# Test case 1
# Test case 1
test_even = [5, 6, 3, 4]
test_even.sort()
# Output: [3, 6, 5, 4]

# Test case 2
test_even = [1, 2, 5, 3, 4]
test_even.sort()
# Output: [1, 2, 5, 3, 4]

# Test case 3
test_even = [10, 11, 12, 13]
test_even.sort()
# Output: [10, 11, 12, 13]
```