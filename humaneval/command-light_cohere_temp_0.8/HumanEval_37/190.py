```python
def sort_even(lst):
    even_set = set(lst[::index(i) for i in range(len(lst)) if i % 2 == 0])
    lst[:] = [i for i in even_set]
    return lst

# test cases
print(sort_even([1, 2, 3]))      # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```  This function takes a list `lst` and uses a generator expression to filter out even indices. The even indices are stored in the set `even_set`, and the original elements are then assigned to the corresponding indices in the original list.