```python
def sorted_list_sum(lst):
    lst_new = []
    for string in lst:
        if len(string) % 2 == 0:
            lst_new.append(string)
    lst_new.sort()
    for i in range(len(lst_new)):
        if i > 0 and lst_new[i] == lst_new[i - 1]:
            del lst_new[i]
    return lst_new
```
The solution uses a simple iterative loop to filter strings that have even lengths and collect them in the `lst_new` list. Then the list is sorted in ascending order based on the even length rule, and finally, all duplicates are deleted. The resulting list is returned. 

*Note*: There is room for improvement in the code's complexity, as the code writes it in linear time complexity, but it can be optimized to run in O(n * log(n)) with the use of the heapq library.