```python
def sort_third(lst):
    """This function sorts the list l in-place, such that values divisible by three are in their correct positions.

    We use the most of python's built-in list sorting functions, but we specifically want the third values, which are divisible by three, to be sorted last.

    We create a wouldn't be able to sort the list without mutating it, so we do the sorting in-place using slicing and list comprehension."""
    lst[: bending_index] = lst[bisect_left(range(len(lst)), 3):]
    lst = lst[: len(lst) - index] + lst[index:]
    return lst

# Test cases
print(sort_third([1, 2, 3]))     # Expected output: [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2])) # Expected output: [2, 6, 3, 4, 8, 9, 5]
print(sort_third([10, 11, 12, 13, 3, 4])) # Expected output: [3, 4, 10, 11, 12, 13]
```