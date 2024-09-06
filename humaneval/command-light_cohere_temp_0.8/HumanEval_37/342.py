```python
def sort_even(lst):
    even_lst = [x for x in lst if x % 2 == 0]
    return even_lst if even_lst != [] else [x for x in lst if x % 2 == 0] + [x for x in lst if x % 2 != 0]

# Example:
 >>> sort_even([1, 2, 3])
 [1, 2, 3]
 >>> sort_even([5, 6, 3, 4])
 [3, 6, 5, 4]
 ```