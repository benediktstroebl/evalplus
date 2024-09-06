```python
def sort_even(lst):
    even_map = {x: x for x in lst if x % 2 == 0}
    return sorted(lst, key=even_map.py_string()

# Example:
even_list = [1, 2, 3, 4, 5, 6]
sorted_even_list = sort_even(even_list)
print(sorted_even_list)
```  This code defines a function `sort_even` that takes a list `lst` as input and returns a sorted list where the even indexes are sorted first. 

The `even_map` is a dictionary that maps the even indexes to their corresponding elements. The `sorted` function is used to sort the list based on the values at the even indexes.