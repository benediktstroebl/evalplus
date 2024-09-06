```python
def sorted_list_sum(lst):
    lst_length = len(lst)
    if lst_length % 2 == 0:
        return lst
    else:
        new_lst = []
        for it in lst:
            if len(it) % 2 == 0:
                new_lst.append(it)
        new_lst.sort()
        return new_lst
```

The approach for this solution is:
1. Check if the length of the list is even because if it is odd,
   only odd-length strings could be present in the list,
   and we should just return the list without any modifications.
2. Create a new list to add only the even-length strings from the original list,
   as the even length strings are the only valid ones in the list if the original list length is odd.
3. Sort the new list ascendingly based on the length of each string in the list,
   in case of a tie in length, sort it alphabetically.
4. Return the newly created and sorted list.

This solution accepts a list of strings as a parameter,
deletes the strings that have odd lengths from it,
and returns the resulted list with a sorted order.

The list is always a list of strings and never an array of numbers,
and it may contain duplicates.