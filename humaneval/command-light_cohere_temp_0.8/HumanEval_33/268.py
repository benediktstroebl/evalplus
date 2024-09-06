```python
def sort_third(l: list):
    """Sorts a list l of integers into a list l' of values that are not divisible by three.

    Parameters:
        l: list of integers
        l': list of integers
    """
    l = [i for i in l if i % 3 != 0]
    return l

# Test cases
test_list = [1, 2, 3, 6, 4, 5, 8, 9]
test_result = sort_third(test_list)
assert test_result == [2, 6, 3, 4, 8, 9, 5]

test_list2 = [5, 6, 3, 4, 8, 9, 2]
test_result2 = sort_third(test_list2)
assert test_result2 == [2, 6, 3, 4, 8, 9, 5]

test_list3 = [1, 2, 3, 8, 4, 5, 9]
test_result3 = sort_third(test_list3)
assert test_result3 == [2, 6, 3, 4, 8, 9, 5]
```