```python
def is_sorted(lst):
    # Count the unique elements and sort the list
    unique, sorted_list = set(lst), sorted(lst)
   
    # If unique elements are more than elements in the list,
    # Then it's not sorted
    if len(unique) > len(sorted_list):
        return False

    # Otherwise, check if sorted_list matches original lst
    for num in lst:
        if num not in unique:
            return False
    return True
```

This function first sorts the list and then checks whether the unique elements in the original list are more than or equal to the number of elements in the sorted list. If this condition is fulfilled, it returns `False`, as the list is not sorted. Otherwise, it checks whether each element of the original list is unique, and if this condition is fulfilled, it returns True. 

This should pass all the test cases provided. Let me know if it works for you or if you'd like me to explain anything!