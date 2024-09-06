```python
def sort_even(l: list):
    """Sorts a list l of integers so that the odd and even indices
    are in equal, sorted order.
    return [list l with the list of even indices sorted and with
    values at even indices unchanged"""
    return l[:::2] + l[1::2]

# test the function with some sample inputs
test_list = [5, 12, 4, 3, 2]
assert sort_even(test_list) == [2, 3, 4, 5, 12]

test_list2 = [3, 6, 5, 4, 2]
assert sort_even(test_list2) == [2, 4, 5, 6, 3]

test_list3 = [1, 10, 6, 5, 9]
assert sort_even(test_list3) == [9, 10, 6, 5, 1]

test_list4 = [5, ,4, 3, 2]
assert sort_even(test_list4) == [2, 3, 4, 5]
```