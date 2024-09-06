```python
def sort_even(lst):
    even_lst = [x for x in lst if x % 2 == 0]
    return even_lst if even_lst == lst else even_lst

#Test case 1
assert sort_even([1, 2, 3]) == [1, 2, 3]

#Test case 2
assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]

#Test case 3
assert sort_even([11, 22, 33, 55]) == [11, 22, 33, 55]
```