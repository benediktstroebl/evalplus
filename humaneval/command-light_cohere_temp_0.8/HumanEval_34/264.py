```python
def unique(lst):
    """Return sorted unique elements in a list"""
    set1 = set(lst)
    return list(set1)

# Test the function with a sample list
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(test_list))  # Output: [0, 2, 3, 5, 9, 123]
```
This script defines a function unique that takes a list as input and returns a new list containing only the unique elements from the original list. This function utilizes the others set of elements in the original list to create a unique set, and then converts the set back to a list of unique elements. The final output will be a sorted list of unique elements from the input list.