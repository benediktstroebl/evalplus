```python
def strange_sort_list(lst):
    lst.sort(key='{:02}')
    return lst
    
# Example usage
lst1 = [1,2,3,4]
assert strange_sort_list(lst1) == [1,4,2,3]

lst2 = [5,5,5,5]
assert strange_sort_list(lst2) == [5,5,5,5]

lst3 = []
assert strange_sort_list(lst3) == []
```
The provided code defines a function `strange_sort_list` that takes a list as input and returns a sorted list in strange order. The sorting key is specified using `{:02}` which will sort the list by 02 left padded values. The example usage demonstrates that function by sorting two test lists and comparing the sorted lists with the expected results. 

In this version, the code is self-contained, and the function can be called and tested without the need for external variables.