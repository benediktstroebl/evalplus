```python
def sort_even(lst):
    even_lst = [x for x in lst if x % 2 == 0]
    res = [x for x in lst if x % 2 == 0]
    res.extend(even_lst)
    return res

# Test cases
test_list1 = [1, 2, 3]
test_list2 = [5, 6, 3, 4]
test_list3 = [2, 9, 8, 7]
test_list4 = [10, 11, 9, 8]

assert sort_even(test_list1) == [1, 2, 3]
assert sort_even(test_list2) == [3, 6, 5, 4]
assert sort_even(test_list3) == [2, 8, 7]
assert sort_even(test_list4) == [8, 10, 9]
 ```