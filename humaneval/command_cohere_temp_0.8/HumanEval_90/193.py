```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
This Python script defines a function called `next_smallest` that takes in a list of integers as input. It sorts the list in ascending order and checks if the length of the list is less than 2. If the list is empty or contains only one element, it returns `None`, indicating that there is no second smallest element. However, if there are two or more elements in the list, it returns the second element, as it is the second smallest element in the sorted list.

Here is a simpler alternative:
```python
def next_smallest(lst):
    return sorted(lst)[1] if len(lst) > 1 else None
```
This version uses Python's built-in sorted() function to sort the list and then retrieves the second element from the sorted list. It also includes a condition to check if the list has more than one element, to avoid errors when calling the function with a single-element list.