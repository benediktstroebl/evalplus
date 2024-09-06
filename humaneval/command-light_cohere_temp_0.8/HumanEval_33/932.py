```python
def sort_third(lst):
    """This function sorts a list l such that values at indices divisible by three are in their original order, while the other values are sorted normally."""
    lst[:] = sorted((x for x in lst if x % 3 != 0), reverse=True) + lst[::3]
    return lst

# Test cases
test_sort_third = []
test_sort_third.add([1, 2, 3)
test_sort_third.add([5, 6, 3, 4, 8, 9, 2)
test_sort_third.add([10, 11, 12)
test_sort_third.add([15, 19, 17, 16, 18, 13, 14)

# Call the function and assert the results
assertEqual(sort_third([1, 2, 3]), [1, 2, 3])
assertEqual(sort_third([5, 6, 3, 4, 8, 9, 2]), [2, 6, 3, 4, 8, 9, 5])
assertEqual(sort_third([10, 11, 12, 13, 14, 15, 19, 17, 16]), [10, 11, 12, 13, 14, 15, 19, 17, 16])
```
The code defines a function `sort_third` that sorts a list such that values at indices divisible by three are in their original order, while the other values are sorted normally. It then adds test cases to check if the function correctly sorts the list according to the specified criteria. 

Finally, it calls the function with the test lists and asserts the results against the expected results using `assertEqual`.