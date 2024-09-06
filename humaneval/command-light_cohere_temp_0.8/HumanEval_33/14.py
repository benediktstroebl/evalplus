```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.

    :return l if the think list
    """
def test_sort_third(test_list):
    test_list = [5, 6, 3, 4, 8, 9, 2]
    result = sort_third(test_list)
    assert result == [2, 6, 3, 4, 8, 9, 5]
    return result

# Driver code
test_list = [5, 6, 3, 4, 8, 9, 2]
sorted_result = test_sort_third(test_list)
print(sorted_result)
```