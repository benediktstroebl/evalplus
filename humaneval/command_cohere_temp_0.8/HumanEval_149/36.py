```python
def sorted_list_sum(lst):
    lst_new = []
    for el in lst:
        if len(el) % 2 == 0:
            lst_new.append(el)
    lst_new.sort()
    for el in lst_new:
        if el != lst_new[0]:
            break
    return lst_new[:len(lst_new) - 1]
```
This function iterates over the list it had received, adding the elements to a new list if the length of the current element used in the list is even. After that, the new list is sorted in ascending order. The function then iterates over the newly sorted list, stopping at the first element that is not the earliest element in the sorted list (i.e., the first element if the list was only one element long, the second if the list had two elements, and so on). The function then returns all elements in the list up to the point where we stopped iterating, essentially deleting the earliest element in the sorted list and returning the remaining elements in their sorted order. This process aligns with the assertions provided in the prompt and should output the desired result.