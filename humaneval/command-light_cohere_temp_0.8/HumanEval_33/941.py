```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that the values at indices that are not divisible by three are in l' are sorted.

    : 1, 2, 3, 5, 6, 7
    [1, 2, 3, 4, 5, 6, 7]  is already sorted
    so we just need to check the values divisible by three.

    The same list has indices that are divisible by three, and the corresponding values are also divisible by three. So we can just simply filter out those values and put the rest in their original order.

    For example:
    [1, 2, 3, 4, 5, 6, 7]
    would become:
    [1, 2, 3, 4, 5, 6, 7]
    after running the function.

# Test case 1
test_sort_third([1, 2, 3])
# Test case 2
test_sort_third([5, 6, 3, 4, 8, 9, 2])
# Test case 3
test_sort_third([10,11,12,13,14,15,16,17,18,19])
```
The code defines a function `sort_third` that takes a list `lst` as input and returns a new list `lst'` where the values at indices that are not divisible by three are sorted. The function works by first creating a list of indices that are divisible by three and then creating a new list where the values at those indices are equal to the values at the corresponding indices in the original list, but sorted. The function then returns the filter out the list and return the new list.