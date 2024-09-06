```python
def sort_third(lst):
    """Sorts the list l such that all values divisible by three appear at the beginning and the end."""
    lst[::3] = lst[::3].extend(lst[1::3])
    lst[1::3] = lst[1::3].extend(lst[2::3])
    return lst

# Test the function with some sample lists
test_sort_third = [
    [1, 2, 3],
    [5, 6, 3, 4, 8, 9, 2],
    [10, 20, 30, 40, 50, 70, 60]
]

print("Sorted list with values divisible by three at the beginning:")
    print(sort_third(test_sort_third))

print("Sorted list with values divisible by three at the end:")
    print(sort_third(test_sort_third[::-1]))
```