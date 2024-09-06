```python
def sorted_list_sum(lst):
    lst_length = len(lst)
    if lst_length % 2 == 0:
        return lst
    else:
        odd_len_index = [i for i, x in enumerate(lst) if len(x) % 2 == 1]
        remove_indices = [i for i in odd_len_index if i != lst_length // 2]
        removable_elements = [lst[i] for i in remove_indices]
        removable_elements.reverse()
        final_list = [x for x in lst if x not in removable_elements]
        final_list.extend(removable_elements)
        final_list.sort()
        final_list.reverse()
        return final_list
```

The approach for the function `sorted_list_sum` is to first determine whether there is any element in the list that has an odd length, and if not, return the original list. Otherwise, we find the indices of the odd-length elements, filter the one at the middle and the others on both sides of the list, reverse them to maintain order, and then remove them from the list. Then, we extend the list with the removable elements, sort them, and reverse them again to get the desired order, and return the list.

Note: the assumption of the problem is that all list elements are strings, and thus the program assumes that it operates with strings, and does not check for other types of elements. This may cause unexpected errors if the list contains other element types.