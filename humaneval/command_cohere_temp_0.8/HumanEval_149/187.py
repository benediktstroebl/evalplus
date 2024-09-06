```python
def sorted_list_sum(lst):
    lst_new = []
    for el in lst:
        if len(el) % 2 == 0:
            lst_new.append(el)
    # sort
    lst_new.sort(key=lambda x: (len(x), x))
    return lst_new
```
This script uses a simple approach that checks for each element in the list whether its length has an even integer division (which means its length is not odd), and if so, it appends it to a new list. After all, iterations are completed, the new list is sorted using the sorting algorithm and a key parameter that defines the sorting logic; in our case, we sort the list by the length of each element, and if the length is the same, we sort it alphabetically. This way, we achieve the desired sorted list that complies with the problem statement.