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
This code snippet defines a function sort_third, which takes a list l and returns a list l’. The function sorts the values of l at indices that are divisible by three and keeps the values at other indices unchanged. To do this, it first creates a copy of the input list l and then iterates through the indices of l. If the current index is divisible by three, it appends the sorted version of the corresponding element in l_copy to the new list sorted_l. Otherwise, it appends the original element from l_copy to sorted_l. Finally, the function returns sorted_l.