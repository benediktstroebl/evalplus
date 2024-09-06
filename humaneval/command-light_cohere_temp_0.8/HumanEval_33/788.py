```python
def sort_third(lst):
    """Sorts the list such that values that are not divisible by three are at the beginning.

    # Sorting
    values that are divisible by three
    new_lst = []
    for i in range(len(lst)):
        if lst[i] % 3 != 0:
            new_lst.append(lst[i])

    # Sorting the remaining values that are divisible by three
    for i in range(len(lst)):
        if lst[i] % 3 == 0:
            new_lst.append(lst[i])

    # Concatenate the sorted values that are not divisible by three and the values that are divisible by three to make lst'
    return new_lst

# Test cases
test_sort_third = []
test_sort_third.append([5, [1, 2, 3])
test_sort_third.append([5, [5, 6, 3, 4, 8, 9, 2])
test_sort_third.append([6, [10, 15, 7, 12, 18, 5])

# Call the function and compare the results
print(sort_third(test_run))
```