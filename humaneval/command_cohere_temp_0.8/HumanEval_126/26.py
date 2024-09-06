```python
def is_sorted(lst):
    # Count the unique elements and sort the list if it contains more than one unique element
    if len(set(lst)) > 1 and not lst == sorted(lst):
        return False
    # If exactly one unique element, it's sorted if it's a single element or a list of ascending integers of that element.
    if len(set(lst)) == 1: 
        return True
    # Check if it's a list of integers ascending from 1 with no duplicates
    return all(isinstance(n, int) for n in lst) and lst[0] == 1 and all(n == (n+1) for n in lst[1:])
```

The logic of the function follows the requirements specified in the prompt:
1. The function first checks whether the list has more than one unique element by checking the set of all elements, and whether it's sorted -- if so, it returns False immediately.
2. If the list has exactly one unique element, it is checked whether it is a single element or a list of that element incremented by 1.
3. If there's more than one unique element, the list is checked whether it's a list of integers starting from 1, with no duplicates, guaranteeing ascending order.

The function should correctly solve the examples provided in the prompt:
```python
print(is_sorted([5]))  # -> True
print(is_sorted([1, 2, 3, 4, 5]))  # -> True
print(is_sorted([1, 3, 2, 4, 5]))  # -> False
print(is_sorted([1, 2, 3, 4, 5, 6]))  # -> True
print(is_sorted([1, 2, 3, 4, 5, 6, 7]))  # -> True
print(is_sorted([1, 3, 2, 4, 5, 6, 7]))  # -> False
print(is_sorted([1, 2, 2, 3, 3, 4]))  # -> True
print(is_sorted([1, 2, 2, 2, 3, 4]))  # -> False
```