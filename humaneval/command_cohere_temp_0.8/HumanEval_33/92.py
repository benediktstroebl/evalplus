```python
def sort_third(l: list):
    l_new = []
    for i in range(len(l)):
        if i % 3 == 0:
            l_new.append(sorted([l[i]]))
        else:
            l_new.append(l[i])
    return l_new
```
This code defines a function sort_third which takes a list as an argument. It creates a new list l_new with the same length as the input list l. For each index i in the list, if the index is divisible by three, it appends a sorted list containing only the element at index i to the new list. Otherwise, it appends the original value at index i. Finally, it returns the new list l_new.