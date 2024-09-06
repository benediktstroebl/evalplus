```python
def sort_third(l: list):
    l_copy = l.copy()
    sorted_l = []
    for i in range(len(l)):
        if i % 3 == 0:
            sorted_l.append(sorted(l_copy[i]))
        else:
            sorted_l.append(l_copy[i])
    return sorted_l
```
This script defines a function sort_third which takes a list l as input and returns a list l’. The function sorts the values in list l at indices that are divisible by three and keeps the other values unchanged. To do this, the script creates a copy of the input list l and uses a loop to iterate through the indices. If the current index is divisible by three, the script sorts a copy of the value at that index and appends it to the new list. For all other cases, the script appends the value at the current index to the new list unchanged.