```python
def sort_even(lst):
    even_lst = [x for x in lst if x % 2 == 0]
    return even_lst

even_lst = sort_even([1, 2, 3])
 assert even_lst == [1, 2, 3]
 even_lst = sort_even([5, 6, 3, 4])
 assert even_lst == [3, 6, 5, 4]
```