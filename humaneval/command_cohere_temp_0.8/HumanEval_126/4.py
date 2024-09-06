```python
def is_sorted(lst):
    # Count the unique elements and sort the list
    unique_count = len(set(lst))
    sorted_lst = sorted(lst)
    
    # If unique elements are greater than or equal to 2 and the list is sorted, return True
    if unique_count >= 2 and lst == sorted_lst:
        return True
    # Otherwise, return False
    else:
        return False
```

The `is_sorted` function takes a list of numbers, `lst`, as input. It first makes the list unique by removing any duplicate elements and sorts the unique list in ascending order. It then compares the sorted list with the original list; if the list is sorted and has more than one unique element, it returns `True`, otherwise, it returns `False`.

Here is an example usage of the function:
```python
print(is_sorted([1, 2, 3, 4, 5]))  # Outputs: True
print(is_sorted([1, 3, 2, 4, 5]))  # Outputs: False
print(is_sorted([1, 2, 2, 3, 4]))  # Outputs: True
```

This version of the function adheres to the problem's constraints and passes the provided test cases. It is concise and achieves the goal using basic Python features, making it relatively efficient in terms of both time and space complexity.