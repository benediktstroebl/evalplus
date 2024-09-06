```python
def sort_third(lst):
    """This function sorts a list l such that elements divisible by three appear first.
    return a value of l[:]
    for i in range(len(l)):
        if lst[i] % 3 == 0:
            lst[i], lst[i] = lst[i], -lst[i]
    return lst

# Test cases
test_sort = [sort_third([1, 2, 3])] == [1, 2, 3]
test_sort = [sort_third([5, 6, 3, 4, 8, 9, 2])] == [2, 6, 3, 4, 8, 9, 5]
test_sort = [sort_third([10, 11, 12])]
test_sort = [sort_third([1, 2, 4, 3, 5, 6])]
test_sort = [sort_third([9, 8, 7, 6])]
test_sort = [sort_third([1, 2, 3, 4, 8, 9])]
```